import os
import json
import sys
from collections import defaultdict

def analyze_test_results(results_file_path):
    """
    分析测试结果文件，统计所有测试用例都通过的问题占比
    
    Args:
        results_file_path: 测试结果JSON文件路径
    """
    try:
        # 读取测试结果文件
        with open(results_file_path, 'r', encoding='utf-8') as f:
            results_data = json.load(f)
        
        # 统计数据
        total_problems = len(results_data)
        all_passed_problems = 0
        
        # 记录通过的问题ID
        passed_problem_ids = []
        
        # 错误类型统计
        error_types = defaultdict(int)
        
        # 遍历所有问题
        for problem_id, problem_data in results_data.items():
            # 获取最新的测试结果（历史记录的最后一项）
            latest_test = problem_data["history"][-1]
            
            # 测试结果从索引1开始（索引0是测试次数）
            # 在新格式中，测试结果可能包含额外的错误信息
            # 我们只需要考虑布尔值部分
            test_results = []
            for i in range(1, len(latest_test)):
                if isinstance(latest_test[i], bool):
                    test_results.append(latest_test[i])
                elif i > len(test_results) and isinstance(latest_test[i], str) and latest_test[i]:
                    # 这是一个错误信息，统计错误类型
                    error_type = latest_test[i].split(":")[0] if ":" in latest_test[i] else latest_test[i]
                    error_types[error_type] += 1
            
            # 检查是否所有测试用例都通过
            if all(test_results):
                all_passed_problems += 1
                passed_problem_ids.append(problem_id)
        
        # 计算通过率
        pass_rate = (all_passed_problems / total_problems) * 100 if total_problems > 0 else 0
        
        # 打印统计结果
        print(f"\n{'='*50}")
        print(f"测试结果分析")
        print(f"{'='*50}")
        print(f"总问题数: {total_problems}")
        print(f"全部测试用例通过的问题数: {all_passed_problems}")
        print(f"通过率: {pass_rate:.2f}%")
        
        # 打印通过的问题ID列表
        print(f"\n通过的问题ID列表:")
        # 每行打印10个ID，使输出更整洁
        for i in range(0, len(passed_problem_ids), 10):
            print(", ".join(passed_problem_ids[i:i+10]))
        
        # 打印错误类型统计
        if error_types:
            print(f"\n错误类型统计:")
            for error_type, count in sorted(error_types.items(), key=lambda x: x[1], reverse=True):
                print(f"{error_type}: {count}次")
        
        # 返回统计结果
        return {
            "total_problems": total_problems,
            "all_passed_problems": all_passed_problems,
            "pass_rate": pass_rate,
            "passed_problem_ids": passed_problem_ids,
            "error_types": dict(error_types)
        }
        
    except Exception as e:
        print(f"分析测试结果时出错: {str(e)}")
        return None

def main():
    """主函数"""
    # 如果没有提供参数或提供了帮助参数，显示用法说明
    if len(sys.argv) == 1 or sys.argv[1] in ['-h', '--help']:
        print("用法: python analyze_test_results.py [测试结果文件路径]")
        print("示例: python analyze_test_results.py .\\SCoT-results-dsv3\\test_results.json")
        print("\n参数说明:")
        print("  [测试结果文件路径]  - 要分析的测试结果JSON文件路径")
        print("                      默认为 .\\SCoT-results-dsv3\\test_results.json")
        print("\n功能说明:")
        print("  分析测试结果文件，统计所有测试用例都通过的问题占比，并显示错误类型统计")
        
        # 如果是显式请求帮助，则直接返回
        if len(sys.argv) > 1:
            return
    
    # 默认测试结果文件路径
    default_results_path = ".\\SCoT-results-dsv3\\test_results.json"
    
    # 如果命令行参数提供了文件路径，则使用命令行参数
    results_file_path = default_results_path
    if len(sys.argv) >= 2:
        results_file_path = sys.argv[1]
    
    # 检查文件是否存在
    if not os.path.exists(results_file_path):
        print(f"错误: 测试结果文件不存在: {results_file_path}")
        print("请使用 'python analyze_test_results.py -h' 查看帮助信息")
        return
    
    # 分析测试结果
    print(f"正在分析测试结果文件: {results_file_path}")
    analyze_test_results(results_file_path)

if __name__ == "__main__":
    main()