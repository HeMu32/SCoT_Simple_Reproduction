import os
import sys
import json
import time
import re
import random


from typing import Dict, Any, Optional

# 导入现有的函数
from mbpp_tester_from_file import read_jsonl_record, run_test, generate_test_report
from llm_api_call import call_llm, clear_conversation_history

# 从llm_api_call导入移动过去的函数
from llm_api_call import validate_solution, ensure_directory_exists, update_test_results_json

# 导入配置参数
from config import MAX_TOKENS, TEMPERATURE


def read_example(example_id: int, dataset_path: str = "mbpp.jsonl", templates_dir: str = "./Templates/Generated_600_699") -> tuple[Dict[str, Any], str, str]:
    """
    读取MBPP记录, 获得问题, 参考答案
    从本地的模板目录中读取对应SCoT示例

    Args:
        example_id: 示例ID
        dataset_path: MBPP数据集路径
        templates_dir: 模板目录路径
    
    Returns:
        一条 (MBPP问题, 模板SCoT, MBPP解答) 
    """
    # 读取MBPP记录
    task = read_jsonl_record(dataset_path, example_id)
    if not task:
        print(f"错误：无法找到示例ID {example_id}")
        return None, "", ""
    
    # 获取问题描述和参考答案
    task_description = task.get('text', '')
    task_code = task.get('code', '')
    
    # 读取对应的SCoT模板
    template_path = os.path.join(templates_dir, f"template_{example_id}.txt")
    if not os.path.exists(template_path):
        print(f"警告：无法找到示例ID {example_id} 的SCoT模板")
        return task, "", task_code
    
    with open(template_path, 'r', encoding='utf-8') as f:
        scot_content = f.read().strip()
    
    return task, scot_content, task_code


def build_prompt_combined(task: Dict[str, Any], num_examples: int = 3, dataset_path: str = "mbpp.jsonl", templates_dir: str = "./Templates/Generated_600_699") -> str:
    """
    输入: 一组示例 (MBPP问题, MBPP解答), 所提问的MBPP问题
    本方法只负责生成模板, 文件IO由别处处理
    根据MBPP任务中的问题描述和MBPP解答, 构建few-shot代码生成示例

    Prompt结构:
        第一部分: 例子:
        [问题描述: 来自MBPP]
        [参考答案: 来自MBPP]

        (更多例子)

        第二部分: 提问:
        [问题描述: 来自MBPP]

    期望LLM回答: 生成代码实现

    Args:
        task: MBPP任务记录
        num_examples: 示例数量
        dataset_path: MBPP数据集路径
        templates_dir: 模板目录路径

    Returns:
        构建好的提示词
    """
    prompt = "You're an expert python programmer. You need to fulfill a following task.\n"
    prompt += "Before the task you will have a few examples.\n\n"

    available_ids = list(range(600, 700))
    num_examples = min(num_examples, len(available_ids))
    example_ids = random.sample(available_ids, num_examples)

    for i, example_id in enumerate(example_ids):
        example_task, _, example_code = read_example(example_id, dataset_path, templates_dir)
        if not example_task or not example_code:
            continue

        prompt += f"Example {i+1}:\n\n"
        prompt += "'''python\n"

        function_name = extract_function_name_from_tests(example_task)
        function_params = ""
        if function_name:
            code_str = example_task.get('code', '')
            func_match = re.search(r'def\s+' + re.escape(function_name) + r'\s*\((.*?)\):', code_str, re.DOTALL)
            if func_match:
                function_params = func_match.group(1)
            prompt += f"def {function_name}({function_params}): \n"
        prompt += "\t\"\"\" \n"
        prompt += f"\t{example_task.get('text', '')} \n"
        prompt += "\t\"\"\" \n"
        prompt += "\tPass\n"
        prompt += "'''\n\n"

        prompt += "[BEGIN CODE]\n"
        prompt += example_code + "\n"
        prompt += "[END CODE]\n\n"
        prompt += f"(end of example {i+1})\n\n"

    prompt += "Now, please solve the following task:\n\n"
    prompt += "'''python\n"
    function_name = extract_function_name_from_tests(task)
    function_params = ""
    if function_name:
        code_str = task.get('code', '')
        func_match = re.search(r'def\s+' + re.escape(function_name) + r'\s*\((.*?)\):', code_str, re.DOTALL)
        if func_match:
            function_params = func_match.group(1)
        prompt += f"def {function_name}({function_params}): \n"
    prompt += "\t\"\"\" \n"
    prompt += f"\t{task.get('text', '')} \n"
    prompt += "\t\"\"\" \n"
    prompt += "\tPass\n"
    prompt += "'''\n\n"
    prompt += "Please implement the code for the above task. You'll need to put [BEGIN CODE] before your code implementation, and [END CODE] after it.\n"

    return prompt



def save_response(task_id: int, response: str, directory: str = "./ans_cache/"):
    """
    保存LLM的回答，并删除带有assert关键字的行
    
    Args:
        task_id: 任务ID
        response: LLM的回答
        directory: 保存目录
    """
    # 确保目录存在
    ensure_directory_exists(directory)
    
    # 检查响应是否包含错误信息
    if response.startswith("调用API时出错:"):
        # 如果是错误响应，直接保存错误信息
        file_path = os.path.join(directory, f"solution_{task_id}.py")
        with open(file_path, 'w', encoding='utf-8') as f:
            f.write(f"# {response}\n# 请重新运行以尝试获取解决方案")
        
        # 同时保存完整错误信息
        full_response_path = os.path.join(directory, f"full_response_{task_id}.txt")
        with open(full_response_path, 'w', encoding='utf-8') as f:
            f.write(response)
        
        return file_path, full_response_path
    
    # 正常处理有效响应
    import re
    code = ""
    
    # 1. 首先尝试提取[BEGIN]和[DONE]之间的代码
    begin_done_match = re.search(r'\[BEGIN\](.*?)\[DONE\]', response, re.DOTALL)
    if begin_done_match:
        extracted_content = begin_done_match.group(1).strip()
        
        # 检查提取的内容是否包含Markdown代码块
        md_match = re.search(r'```(?:python)?\s*(.*?)\s*```', extracted_content, re.DOTALL)
        if md_match:
            # 如果[BEGIN]/[DONE]内部还有Markdown代码块，提取其中的代码
            code = md_match.group(1).strip()
        else:
            # 否则直接使用[BEGIN]/[DONE]之间的内容
            code = extracted_content
    else:
        # 2. 如果没有[BEGIN]/[DONE]标记，尝试提取Markdown代码块
        md_match = re.search(r'```(?:python)?\s*(.*?)\s*```', response, re.DOTALL)
        if md_match:
            code = md_match.group(1).strip()
        else:
            # 3. 如果都没找到，就保存整个回答
            code = response
    
    # 删除带有assert关键字的行
    code_lines = code.split('\n')
    filtered_code_lines = [line for line in code_lines if 'assert' not in line]
    code = '\n'.join(filtered_code_lines)
    
    # 保存到文件
    file_path = os.path.join(directory, f"solution_{task_id}.py")
    with open(file_path, 'w', encoding='utf-8') as f:
        f.write(code)
    
    # 同时保存完整回答（用于调试）
    full_response_path = os.path.join(directory, f"full_response_{task_id}.txt")
    with open(full_response_path, 'w', encoding='utf-8') as f:
        f.write(response)
    
    return file_path, full_response_path



def solve_mbpp_task_FewShot(task_id: int, dataset_path: str = "mbpp.jsonl", validate_immediately: bool = True, result_dir: str = ".\\SCoT-results-dsv3", timeout: int = 10):
    """
    解决MBPP任务
    Args:
        task_id: 任务ID
        dataset_path: MBPP数据集路径
        validate_immediately: 是否立即验证解答的正确性
        result_dir: 结果保存目录
        timeout: 测试超时时间（秒），默认为10秒
    Returns:
        解答文件路径

    新的Prompt生成方式:
        随机抽取i个序号, 范围600-699
        分别读取这i个序号对应的 (MBPP问题, 模板SCoT, MBPP解答) 
        读取当前测试的MBPP问题
        将当前的问题和i个示例传递给Prompt构建方法, 一步获得SCoT和代码
        *保存SCoT和代码
        *测试代码
        *保存测试结果
    """
    # 确保结果目录存在
    ensure_directory_exists(result_dir)

    # 读取任务
    task = read_jsonl_record(dataset_path, task_id)
    if not task:
        print(f"错误：无法找到任务ID {task_id}")
        return None
    
    # 构建用于一步获取SCoT和代码的提示词
    combined_prompt = build_prompt_combined(task)
    
    # 使用这个Prompt询问LLM
    print(f"正在请求LLM生成解题思路和代码实现 (任务 {task_id})...")
    conversation_history = clear_conversation_history()
    combined_response, _ = call_llm(combined_prompt, conversation_history, max_tokens=MAX_TOKENS)
    
    # 提取SCoT部分和代码部分
    import re
    
    # 提取SCoT
    scot_match = re.search(r'\[BEGIN PROCESS\](.*?)\[END PROCESS\]', combined_response, re.DOTALL)
    scot_content = ""
    if scot_match:
        scot_content = scot_match.group(1).strip()
    
    # 提取代码
    code_match = re.search(r'\[BEGIN CODE\](.*?)\[END CODE\]', combined_response, re.DOTALL)
    code_content = ""
    if code_match:
        code_content = code_match.group(1).strip()
    
    # 如果没有找到标记，尝试其他可能的格式
    if not scot_content:
        # 尝试查找[BEGIN]和[DONE]标记
        scot_match_alt = re.search(r'\[BEGIN\](.*?)\[DONE\]', combined_response, re.DOTALL)
        if scot_match_alt:
            scot_content = scot_match_alt.group(1).strip()
    
    if not code_content:
        # 尝试查找```python和```标记
        code_match_alt = re.search(r'```(?:python)?\s*(.*?)\s*```', combined_response, re.DOTALL)
        if code_match_alt:
            code_content = code_match_alt.group(1).strip()
    
    # 保存SCoT部分
    if scot_content:
        scot_file_path = os.path.join(result_dir, f"scot_{task_id}.txt")
        with open(scot_file_path, 'w', encoding='utf-8') as f:
            f.write(scot_content)
        print(f"SCoT解题思路已保存到: {scot_file_path}")
    else:
        print("警告：无法从回复中提取SCoT解题思路")
    
    # 保存完整回答
    full_response_path = os.path.join(result_dir, f"full_response_{task_id}.txt")
    with open(full_response_path, 'w', encoding='utf-8') as f:
        f.write(combined_response)
    print(f"完整回答已保存到: {full_response_path}")
    
    # 保存代码部分
    solution_path = None
    if code_content:
        # 删除带有assert关键字的行
        code_lines = code_content.split('\n')
        filtered_code_lines = [line for line in code_lines if 'assert' not in line]
        code_content = '\n'.join(filtered_code_lines)
        
        solution_path = os.path.join(result_dir, f"solution_{task_id}.py")
        with open(solution_path, 'w', encoding='utf-8') as f:
            f.write(code_content)
        print(f"代码解答已保存到: {solution_path}")
        
        # 测试答案
        if validate_immediately and solution_path:
            print("\n正在验证解答...")
            validate_solution(solution_path, task_id, task, result_dir=result_dir, timeout=timeout)
    else:
        print("警告：无法从回复中提取代码实现")
    
    return solution_path

def batch_solve_mbpp_tasks(start_id: int, end_id: int, dataset_path: str = "mbpp.jsonl", delay: int = 15, result_dir: str = ".\\SCoT-results-dsv3", timeout: int = 10):
    """
    批量解决MBPP任务
    
    Args:
        start_id: 起始问题ID
        end_id: 结束问题ID
        dataset_path: MBPP数据集路径
        delay: 每个问题之间的延迟时间（秒）
        result_dir: 结果保存目录
        timeout: 测试超时时间（秒），默认为10秒
    """
    # 确保结果目录存在
    ensure_directory_exists(result_dir)
    
    # 创建一个摘要文件，记录所有问题的测试结果
    summary_path = os.path.join(result_dir, "test_summary.json")
    summary = {}
    
    # 创建一个统一的测试结果文件
    test_results_path = os.path.join(result_dir, "test_results.json")
    
    # 加载现有的摘要（如果存在）
    if os.path.exists(summary_path):
        try:
            with open(summary_path, 'r', encoding='utf-8') as f:
                summary = json.load(f)
        except json.JSONDecodeError:
            summary = {}
    
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
            print(f"警告：无法找到任务ID {task_id}，跳过")
            continue
        
        # 检查是否已经处理过
        task_id_str = str(task_id)
        if task_id_str in summary and summary[task_id_str].get("completed", False):
            print(f"任务 {task_id} 已经处理过，跳过")
            continue
        
        try:
            # 解决任务
            solution_path = solve_mbpp_task_FewShot(task_id, dataset_path, validate_immediately=True, result_dir=result_dir, timeout=timeout)
            
            # 更新摘要
            if solution_path:
                # 重新加载测试结果文件，获取最新的测试结果
                test_results_data = {}
                if os.path.exists(test_results_path):
                    try:
                        with open(test_results_path, 'r', encoding='utf-8') as f:
                            test_results_data = json.load(f)
                    except json.JSONDecodeError:
                        test_results_data = {}
                
                # 检查测试结果: 存在Bug
                if task_id_str in test_results_data:
                    test_results = test_results_data[task_id_str]
                    all_passed = all(test.get("passed", False) for test in test_results.get("tests", []))
                    
                    summary[task_id_str] = {
                        "completed": True,
                        "all_tests_passed": all_passed,
                        "solution_path": solution_path
                    }
                    
                    # 保存摘要
                    with open(summary_path, 'w', encoding='utf-8') as f:
                        json.dump(summary, f, indent=2)
                    
                    print(f"任务 {task_id} 完成，测试{'全部通过' if all_passed else '未全部通过'}")
                else:
                    print(f"警告：无法找到任务 {task_id} 的测试结果，但解答已保存")
                    # 即使没有找到测试结果，也标记为已完成
                    summary[task_id_str] = {
                        "completed": True,
                        "all_tests_passed": None,  # 未知是否通过
                        "solution_path": solution_path
                    }
                    
                    # 保存摘要
                    with open(summary_path, 'w', encoding='utf-8') as f:
                        json.dump(summary, f, indent=2)
        except Exception as e:
            print(f"处理任务 {task_id} 时出错: {e}")
        
        # 延迟一段时间，避免API调用过于频繁
        if task_id < end_id:
            print(f"等待 {delay} 秒后继续...")
            time.sleep(delay)
    
    # 记录结束时间和总用时
    end_time = time.time()
    total_time = end_time - start_time
    print(f"\n{'='*50}")
    print(f"批量处理完成！")
    print(f"处理范围: {start_id} - {end_id}")
    print(f"总用时: {total_time:.2f} 秒")
    print(f"{'='*50}")

def main():
    """主函数"""
    if len(sys.argv) < 2:
        print("用法: python mbpp_llm_solver_SCoT.py <task_id> [dataset_path] [validate] [result_dir]")
        print("或者: python mbpp_llm_solver_SCoT.py batch <start_id> <end_id> [dataset_path] [delay] [result_dir]")
        print("例如: python mbpp_llm_solver_SCoT.py 6")
        print("例如: python mbpp_llm_solver_SCoT.py batch 11 20")
        print("validate: true - 立即验证解答(默认), false - 不验证解答")
        print("delay: 每个问题之间的延迟时间（秒），默认为15")
        print("result_dir: 结果保存目录，默认为.\\SCoT-results-dsv3")
        sys.exit(1)

    # 检查是否为批量模式
    if sys.argv[1].lower() == "batch":
        if len(sys.argv) < 4:
            print("批量模式用法: python mbpp_llm_solver_SCoT.py batch <start_id> <end_id> [dataset_path] [delay] [result_dir]")
            sys.exit(1)
        
        try:
            start_id = int(sys.argv[2])
            end_id = int(sys.argv[3])
        except ValueError:
            print("错误: 问题ID必须是整数")
            sys.exit(1)
        
        # 默认数据集文件路径
        dataset_path = "mbpp.jsonl"
        if len(sys.argv) >= 5:
            dataset_path = sys.argv[4]
        
        # 默认延迟时间
        delay = 15
        if len(sys.argv) >= 6:
            try:
                delay = int(sys.argv[5])
            except ValueError:
                print(f"警告: 延迟时间必须是整数，使用默认值{delay}")
        
        # 默认结果保存目录
        result_dir = ".\\SCoT-results-dsv3"
        if len(sys.argv) >= 7:
            result_dir = sys.argv[6]
            print(f"结果将保存到: {os.path.abspath(result_dir)}")
        else:
            print(f"使用默认结果保存目录: {os.path.abspath(result_dir)}")
        
        print(f"使用延迟时间: {delay}秒")
        
        # 批量解决任务
        batch_solve_mbpp_tasks(start_id, end_id, dataset_path, delay, result_dir)
    else:
        # 单个任务模式
        try:
            task_id = int(sys.argv[1])
        except ValueError:
            print("错误: 任务ID必须是整数")
            sys.exit(1)
        
        # 默认数据集文件路径
        dataset_path = "mbpp.jsonl"
        if len(sys.argv) >= 3:
            dataset_path = sys.argv[2]
        
        # 是否立即验证
        validate_immediately = True
        if len(sys.argv) >= 4:
            validate_immediately = sys.argv[3].lower() == "true"
        
        # 默认结果保存目录
        result_dir = ".\\SCoT-results-dsv3"
        if len(sys.argv) >= 5:
            result_dir = sys.argv[4]
            print(f"结果将保存到: {os.path.abspath(result_dir)}")
        else:
            print(f"使用默认结果保存目录: {os.path.abspath(result_dir)}")
        
        # 解决任务
        solution_path = solve_mbpp_task_FewShot(task_id, dataset_path, validate_immediately, result_dir)
        
        if solution_path:
            print(f"\n任务 {task_id} 已完成！")
            if not validate_immediately:
                print(f"你可以使用以下命令测试解答:")
                print(f"python mbpp_tester_from_file.py {solution_path} {task_id}")

def extract_function_name_from_tests(task: Dict[str, Any]) -> str:
    """
    从测试用例中提取函数名
    """
    test_list = task.get('test_list', [])
    if not test_list:
        return ""
    for test in test_list:
        func_call_match = re.search(r'(\w+)\(', test)
        if func_call_match:
            return func_call_match.group(1)
    return ""

if __name__ == "__main__":
    main()