import os
import sys
import time
import json
from typing import Dict, Any, List, Optional

# 导入现有的函数
from mbpp_tester_from_file import read_jsonl_record
from mbpp_llm_solver import solve_mbpp_task_zero_shot
from llm_api_call import ensure_directory_exists

def batch_test_mbpp(start_id: int, end_id: int, dataset_path: str = "c:\\Users\\HeMu\\Desktop\\SCoT-Rep\\mbpp.jsonl", 
                   result_dir: str = ".\\results\\", delay: int = 5, timeout: int = 10):
    """
    批量测试MBPP问题
    
    Args:
        start_id: 起始问题ID
        end_id: 结束问题ID
        dataset_path: MBPP数据集路径
        result_dir: 结果保存目录
        delay: 每个问题之间的延迟时间（秒）
        timeout: 测试超时时间（秒），默认为10秒
    """
    # 确保结果目录存在
    ensure_directory_exists(result_dir)
    
    # 创建一个摘要文件，记录所有问题的测试结果
    summary_path = os.path.join(result_dir, "test_summary.json")
    summary = {}
    
    # 创建一个统一的测试结果文件
    test_results_path = os.path.join(result_dir, "test_results.json")
    test_results_data = {}
    
    # 加载现有的摘要和测试结果（如果存在）
    if os.path.exists(summary_path):
        try:
            with open(summary_path, 'r', encoding='utf-8') as f:
                summary = json.load(f)
        except json.JSONDecodeError:
            summary = {}
    
    if os.path.exists(test_results_path):
        try:
            with open(test_results_path, 'r', encoding='utf-8') as f:
                test_results_data = json.load(f)
        except json.JSONDecodeError:
            test_results_data = {}
    
    # 记录开始时间
    start_time = time.time()
    
    # 遍历问题ID范围
    for task_id in range(start_id, end_id + 1):
        print(f"\n{'='*50}")
        print(f"开始处理任务 {task_id}")
        print(f"{'='*50}")
        
        # 检查任务是否存在
        task = read_jsonl_record(dataset_path, task_id)
        if not task:
            print(f"跳过任务 {task_id}：任务不存在")
            continue
        
        try:
            # 解决任务并保存到指定目录 - 移除timeout参数
            solution_path = solve_mbpp_task_zero_shot(task_id, dataset_path, True)
            
            if solution_path:
                # 将解决方案复制到结果目录
                target_solution_path = os.path.join(result_dir, f"solution_{task_id}.py")
                with open(solution_path, 'r', encoding='utf-8') as src:
                    with open(target_solution_path, 'w', encoding='utf-8') as dst:
                        dst.write(src.read())
                
                # 复制完整回答
                src_full_response = os.path.join("./ans_cache/", f"full_response_{task_id}.txt")
                if os.path.exists(src_full_response):
                    target_full_response = os.path.join(result_dir, f"full_response_{task_id}.txt")
                    with open(src_full_response, 'r', encoding='utf-8') as src:
                        with open(target_full_response, 'w', encoding='utf-8') as dst:
                            dst.write(src.read())
                
                # 从ans_cache中读取测试结果并合并到统一的测试结果文件中
                src_test_results = os.path.join("./ans_cache/", "test_results.json")
                if os.path.exists(src_test_results):
                    with open(src_test_results, 'r', encoding='utf-8') as src:
                        src_data = json.load(src)
                        if str(task_id) in src_data:
                            # 将当前任务的测试结果添加到统一的测试结果数据中
                            test_results_data[str(task_id)] = src_data[str(task_id)]
                            # 保存更新后的测试结果
                            with open(test_results_path, 'w', encoding='utf-8') as f:
                                json.dump(test_results_data, f, indent=2)
                
                # 更新摘要
                summary[str(task_id)] = {
                    "task_description": task.get('text', ''),
                    "solution_path": target_solution_path,
                    "timestamp": time.strftime("%Y-%m-%d %H:%M:%S")
                }
                
                # 保存更新后的摘要
                with open(summary_path, 'w', encoding='utf-8') as f:
                    json.dump(summary, f, indent=2)
                
                print(f"任务 {task_id} 处理完成，结果已保存")
            else:
                print(f"任务 {task_id} 处理失败")
        
        except Exception as e:
            print(f"处理任务 {task_id} 时出错: {str(e)}")
        
        # 延迟一段时间，避免API请求过于频繁
        if task_id < end_id:
            print(f"等待 {delay} 秒后继续下一个任务...")
            time.sleep(delay)
    
    # 记录结束时间和总耗时
    end_time = time.time()
    total_time = end_time - start_time
    hours, remainder = divmod(total_time, 3600)
    minutes, seconds = divmod(remainder, 60)
    
    # 生成统计报告
    generate_statistics_report(result_dir, start_id, end_id)
    
    print(f"\n{'='*50}")
    print(f"批量测试完成")
    print(f"处理范围: {start_id} - {end_id}")
    print(f"总耗时: {int(hours)}小时 {int(minutes)}分钟 {int(seconds)}秒")
    print(f"结果保存在: {os.path.abspath(result_dir)}")
    print(f"{'='*50}")

def generate_statistics_report(result_dir: str, start_id: int, end_id: int):
    """
    通过读取test_results.json文件生成统计报告
    
    Args:
        result_dir: 结果保存目录
        start_id: 起始问题ID
        end_id: 结束问题ID
    """
    # 统计数据
    total_tasks = end_id - start_id + 1
    processed_tasks = 0
    success_tasks = 0
    failed_tasks = 0
    skipped_tasks = 0
    
    # 读取统一的测试结果文件
    test_results_path = os.path.join(result_dir, "test_results.json")
    if os.path.exists(test_results_path):
        try:
            with open(test_results_path, 'r', encoding='utf-8') as f:
                test_data = json.load(f)
                
                # 遍历所有任务ID
                for task_id in range(start_id, end_id + 1):
                    task_id_str = str(task_id)
                    if task_id_str in test_data:
                        processed_tasks += 1
                        # 获取最新的测试结果
                        latest_test = test_data[task_id_str]["history"][-1]
                        # 第一个元素是测试次数，后面的元素是测试结果
                        test_results = latest_test[1:]
                        if all(test_results):
                            success_tasks += 1
                        else:
                            failed_tasks += 1
                    else:
                        skipped_tasks += 1
        except Exception as e:
            print(f"读取测试结果文件时出错: {str(e)}")
    else:
        skipped_tasks = total_tasks
    
    # 计算成功率
    success_rate = (success_tasks / processed_tasks * 100) if processed_tasks > 0 else 0
    
    # 创建统计报告
    stats = {
        "start_id": start_id,
        "end_id": end_id,
        "total_tasks": total_tasks,
        "processed_tasks": processed_tasks,
        "success_tasks": success_tasks,
        "failed_tasks": failed_tasks,
        "skipped_tasks": skipped_tasks,
        "success_rate": f"{success_rate:.2f}%",
        "timestamp": time.strftime("%Y-%m-%d %H:%M:%S")
    }
    
    # 保存统计报告
    stats_file = os.path.join(result_dir, "statistics.json")
    with open(stats_file, 'w', encoding='utf-8') as f:
        json.dump(stats, f, indent=2)
    
    # 打印统计信息
    print(f"\n{'='*50}")
    print(f"测试统计信息")
    print(f"{'='*50}")
    print(f"总任务数: {total_tasks}")
    print(f"已处理任务: {processed_tasks}")
    print(f"成功任务: {success_tasks}")
    print(f"失败任务: {failed_tasks}")
    print(f"跳过任务: {skipped_tasks}")
    print(f"成功率: {success_rate:.2f}%")
    print(f"统计报告已保存到: {stats_file}")

def main():
    """主函数"""
    if len(sys.argv) < 3:
        print("用法: python batch_test_mbpp.py <start_id> <end_id> [dataset_path] [result_dir] [delay]")
        print("例如: python batch_test_mbpp.py 11 510")
        print("      python batch_test_mbpp.py 11 510 c:\\Users\\HeMu\\Desktop\\SCoT-Rep\\mbpp.jsonl .\\custom-results\\")
        print("参数说明:")
        print("  start_id: 起始问题ID")
        print("  end_id: 结束问题ID")
        print("  dataset_path: 数据集路径，默认为c:\\Users\\HeMu\\Desktop\\SCoT-Rep\\mbpp.jsonl")
        print("  result_dir: 结果保存目录，默认为.\\zero-shot-results-dsv3\\")
        print("  delay: 每个问题之间的延迟时间（秒），默认为5秒")
        sys.exit(1)
    
    try:
        start_id = int(sys.argv[1])
        end_id = int(sys.argv[2])
    except ValueError:
        print("错误: 问题ID必须是整数")
        sys.exit(1)
    
    # 默认数据集文件路径
    dataset_path = "c:\\Users\\HeMu\\Desktop\\SCoT-Rep\\mbpp.jsonl"
    if len(sys.argv) >= 4:
        dataset_path = sys.argv[3]
    
    # 默认结果保存目录
    result_dir = ".\\zero-shot-results-dsv3\\"
    if len(sys.argv) >= 5:
        result_dir = sys.argv[4]
        print(f"结果将保存到: {os.path.abspath(result_dir)}")
    else:
        print(f"使用默认结果保存目录: {os.path.abspath(result_dir)}")
    
    # 默认延迟时间
    delay = 5
    if len(sys.argv) >= 6:
        try:
            delay = int(sys.argv[5])
        except ValueError:
            print("警告: 延迟时间必须是整数，使用默认值5秒")
    
    # 执行批量测试 - 保持与函数定义一致，但不传递timeout参数
    batch_test_mbpp(start_id, end_id, dataset_path, result_dir, delay)

if __name__ == "__main__":
    main()