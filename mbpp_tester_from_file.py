import os
import re
import sys
import json
import time
import multiprocessing
from typing import List, Dict, Tuple, Any, Optional

def read_solution_file(solution_file_path: str) -> str:
    """
    从本地文件读取解答代码
    
    Args:
        solution_file_path: 解答代码文件路径
        
    Returns:
        解答代码字符串
    """
    try:
        with open(solution_file_path, 'r', encoding='utf-8') as f:
            return f.read()
    except Exception as e:
        raise ValueError(f"读取解答文件时出错: {e}")

def read_jsonl_record(file_path: str, task_id: int) -> Optional[Dict[str, Any]]:
    """
    从JSONL文件中读取指定任务ID的记录
    
    Args:
        file_path: JSONL文件路径
        task_id: 要读取的任务ID
        
    Returns:
        记录的字典表示，如果任务ID不存在则返回None
    """
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            for line in f:
                record = json.loads(line.strip())
                if record.get('task_id') == task_id:
                    return record
        print(f"错误：任务ID {task_id} 在数据集中不存在")
        return None
    except Exception as e:
        print(f"读取数据集文件时出错: {e}")
        return None

# 用于在子进程中执行测试的函数
def _run_test_in_process(code: str, test_case: str, result_queue):
    """
    在子进程中运行测试用例
    
    Args:
        code: 要测试的代码
        test_case: 测试用例
        result_queue: 用于返回结果的队列
    """
    local_namespace = {}
    try:
        # 执行代码
        exec(code, local_namespace)
        # 执行测试用例 - 移除test_case中的"assert"前缀
        if test_case.startswith("assert "):
            test_case = test_case[7:]  # 移除"assert "前缀
        exec(f"assert {test_case}", local_namespace)
        result_queue.put((True, ""))
    except AssertionError as e:
        result_queue.put((False, f"断言错误: {str(e)}"))
    except Exception as e:
        result_queue.put((False, f"执行错误: {str(e)}"))

def run_test(code: str, test_case: str, timeout: int = 10) -> Tuple[bool, str]:
    """
    运行单个测试用例，带有超时功能
    
    Args:
        code: 要测试的代码
        test_case: 测试用例
        timeout: 超时时间（秒），默认为10秒
        
    Returns:
        测试结果（成功/失败）和错误信息（如果有）
    """
    # 创建一个队列用于获取结果
    result_queue = multiprocessing.Queue()
    
    # 创建子进程运行测试
    process = multiprocessing.Process(
        target=_run_test_in_process,
        args=(code, test_case, result_queue)
    )
    
    # 启动进程
    process.start()
    
    # 等待进程完成或超时
    process.join(timeout)
    
    # 检查进程是否仍在运行（超时）
    if process.is_alive():
        # 终止进程
        process.terminate()
        process.join()
        return False, f"执行超时: 代码执行超过 {timeout} 秒，可能存在死循环或性能问题"
    
    # 获取结果
    if not result_queue.empty():
        return result_queue.get()
    else:
        return False, "执行错误: 未能获取测试结果"

def generate_test_report(task_id: int, test_results: List[Dict[str, Any]]) -> str:
    """
    生成测试报告
    
    Args:
        task_id: 任务ID
        test_results: 测试结果列表
        
    Returns:
        格式化的测试报告
    """
    passed_count = sum(1 for result in test_results if result['passed'])
    total_count = len(test_results)
    
    report = f"""
==================================================
测试结果 - 任务ID: {task_id}
==================================================

总结: 通过 {passed_count}/{total_count} 测试用例
"""
    
    for i, result in enumerate(test_results, 1):
        status = "✅ 通过" if result['passed'] else "❌ 失败"
        report += f"\n测试 {i}: {status}\n"
        report += f"测试用例: {result['test_case']}\n"
        
        if not result['passed']:
            report += f"错误信息: {result['error']}\n"
            if result.get('traceback'):
                report += f"{result['traceback']}\n"
    
    return report

def main():
    """主函数"""
    if len(sys.argv) < 3:
        print("用法: python mbpp_tester_from_file.py <solution_file_path> <task_id> [dataset_path] [output_mode] [timeout]")
        print("例如: python mbpp_tester_from_file.py solution_6.py 6")
        print("output_mode: console - 只输出到控制台, file - 只输出到文件, both - 同时输出到控制台和文件(默认)")
        print("timeout: 测试超时时间（秒），默认为10秒")
        sys.exit(1)
    
    solution_file_path = sys.argv[1]
    try:
        task_id = int(sys.argv[2])
    except ValueError:
        print("错误: 任务ID必须是整数")
        sys.exit(1)
    
    # 默认数据集文件路径
    dataset_path = "c:\\Users\\HeMu\\Desktop\\SCoT-Rep\\mbpp.jsonl"
    if len(sys.argv) >= 4 and not sys.argv[3] in ['console', 'file', 'both']:
        dataset_path = sys.argv[3]
    
    # 默认输出模式为console（只输出到控制台）
    output_mode = 'console'
    if len(sys.argv) >= 5:
        if sys.argv[4] in ['console', 'file', 'both']:
            output_mode = sys.argv[4]
    elif len(sys.argv) == 4 and sys.argv[3] in ['console', 'file', 'both']:
        output_mode = sys.argv[3]
    
    # 默认超时时间为10秒
    timeout = 10
    if len(sys.argv) >= 6:
        try:
            timeout = int(sys.argv[5])
        except ValueError:
            print(f"警告: 超时时间必须是整数，使用默认值{timeout}秒")
    
    try:
        # 读取解答代码
        code = read_solution_file(solution_file_path)
        
        # 从数据集中读取问题和测试用例
        record = read_jsonl_record(dataset_path, task_id)
        if not record:
            sys.exit(1)
        
        # 获取测试用例
        test_cases = record.get('test_list', [])
        if not test_cases:
            print(f"错误: 任务ID {task_id} 没有测试用例")
            sys.exit(1)
        
        # 运行测试
        test_results = []
        for test_case in test_cases:
            passed, error = run_test(code, test_case, timeout)
            test_results.append({
                'test_case': test_case,
                'passed': passed,
                'error': error
            })
        
        # 生成报告
        report = generate_test_report(task_id, test_results)
        
        # 根据输出模式决定输出方式
        if output_mode in ['file', 'both']:
            # 将报告写入文件
            output_file = f"mbpp_test_results_{task_id}_from_file.md"
            with open(output_file, 'w', encoding='utf-8') as f:
                f.write(report)
            
            if output_mode == 'both':
                print(f"测试完成，结果已保存到 {output_file}")
        
        if output_mode in ['console', 'both']:
            # 输出到控制台
            print(report)
        
        # 打印问题描述，方便用户参考
        print("\n问题描述:")
        print(record.get('text', '无描述'))
        
    except Exception as e:
        print(f"错误: {str(e)}")
        sys.exit(1)

if __name__ == "__main__":
    main()