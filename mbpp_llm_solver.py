import os
import sys
import json
import re
import time

from typing import Dict, Any, Optional

# 导入现有的函数
from mbpp_tester_from_file import read_jsonl_record, run_test, generate_test_report
from llm_api_call import call_llm, clear_conversation_history

# 从llm_api_call导入移动过去的函数
from llm_api_call import validate_solution, ensure_directory_exists, update_test_results_json

# 导入配置参数
from config import MAX_TOKENS, TEMPERATURE

# 移除了ensure_directory_exists函数，因为已经移到llm_api_call.py


def extract_function_name(task: Dict[str, Any]) -> str:
    """
    从MBPP记录中提取函数名
    """
    # 首先尝试从代码中提取函数名
    code_str = task.get('code', '')
    if code_str:
        func_match = re.search(r'def\s+(\w+)\s*\(', code_str, re.DOTALL)
        if func_match:
            return func_match.group(1)
    
    return ""


def build_prompt_zero_shot(task: Dict[str, Any]) -> str:
    """
    根据MBPP任务构建提示词
    Args:
        task: MBPP任务记录
    Returns:
        构建好的提示词
    """
    # 提取任务描述
    task_description = task.get('text', '')

    # 提取函数名和参数
    function_name = extract_function_name(task)
    function_params = ""
    code_str = task.get('code', '')
    if function_name and code_str:
        func_match = re.search(r'def\s+' + re.escape(function_name) + r'\s*\((.*?)\):', code_str, re.DOTALL)
        if func_match:
            function_params = func_match.group(1)

    prompt = "You're an expert python programmer. You need to fulfill the following task.\n\n"
    prompt += "'''python\n"
    if function_name:
        prompt += f"def {function_name}({function_params}): \n"
    prompt += "\t\"\"\" \n"
    prompt += f"\t{task_description} \n"
    prompt += "\t\"\"\" \n"
    prompt += "\tPass\n"
    prompt += "'''\n\n"
    prompt += "Please implement the code for the above task. You'll need to put [BEGIN CODE] before your code implementation, and [END CODE] after it.\n"

    prompt += "You don't need to explain your code. Just provide the code. \n"

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
    
    # 1. 尝试提取[BEGIN CODE]和[END CODE]之间的内容
    begin_code_match = re.search(r'\[BEGIN CODE\](.*?)\[END CODE\]', response, re.DOTALL)
    if begin_code_match:
        extracted_content = begin_code_match.group(1).strip()
        # 检查提取的内容中是否有Markdown代码块
        md_match = re.search(r'```(?:python)?\s*(.*?)\s*```', extracted_content, re.DOTALL)
        if md_match:
            code = md_match.group(1).strip()
        else:
            code = extracted_content
    
    # 2. 如果没有找到[BEGIN CODE]标记，尝试提取[BEGIN]和[END]或[DONE]之间的内容
    elif not code:
        begin_match = re.search(r'\[BEGIN\](.*?)(?:\[END\]|\[DONE\])', response, re.DOTALL)
        if begin_match:
            extracted_content = begin_match.group(1).strip()
            # 检查提取的内容中是否有Markdown代码块
            md_match = re.search(r'```(?:python)?\s*(.*?)\s*```', extracted_content, re.DOTALL)
            if md_match:
                code = md_match.group(1).strip()
            else:
                code = extracted_content
    
    # 3. 如果上述都没找到，直接尝试提取Markdown代码块
    if not code:
        md_match = re.search(r'```(?:python)?\s*(.*?)\s*```', response, re.DOTALL)
        if md_match:
            code = md_match.group(1).strip()
        else:
            # 4. 如果都没找到，就保存整个回答
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



def solve_mbpp_task_zero_shot(task_id: int, dataset_path: str = "c:\\Users\\HeMu\\Desktop\\SCoT-Rep\\mbpp.jsonl", validate_immediately: bool = True):
    """
    解决MBPP任务
    Args:
        task_id: 任务ID
        dataset_path: MBPP数据集路径
        validate_immediately: 是否立即验证解答的正确性
    Returns:
        解答文件路径
    """

    # 读取任务
    task = read_jsonl_record(dataset_path, task_id)
    if not task:
        print(f"错误：无法找到任务ID {task_id}")
        return None
    

    # 构建提示词
    prompt = build_prompt_zero_shot(task)

######################################################################################
    print (prompt)
    
    # 清除之前的对话历史
    conversation_history = clear_conversation_history()
    
    # 调用LLM，使用config.py中的参数
    print(f"正在请求LLM解决任务 {task_id}...")

    response, _ = call_llm(prompt, conversation_history, max_tokens=MAX_TOKENS)
 
    # 保存回答
    solution_path, full_response_path = save_response(task_id, response)
    
    print(f"解答已保存到: {solution_path}")
    print(f"完整回答已保存到: {full_response_path}")
    
    # 根据参数决定是否立即验证答案正确性
    if validate_immediately:
        print("\n正在验证解答...")
        validate_solution(solution_path, task_id, task)  # 调用从llm_api_call导入的函数
    return solution_path

# 移除了update_test_results_json函数，因为已经移到llm_api_call.py

# 移除了validate_solution函数，因为已经移到llm_api_call.py

def main():


    """主函数"""
    if len(sys.argv) < 2:

        print("用法: python mbpp_llm_solver.py <task_id> [dataset_path] [validate]")
        print("例如: python mbpp_llm_solver.py 6")
        print("validate: true - 立即验证解答(默认), false - 不验证解答")
        sys.exit(1)

    try:
        task_id = int(sys.argv[1])


    except ValueError:
        print("错误: 任务ID必须是整数")
        sys.exit(1)
    

    # 默认数据集文件路径
    dataset_path = "c:\\Users\\HeMu\\Desktop\\SCoT-Rep\\mbpp.jsonl"
    if len(sys.argv) >= 3:
        dataset_path = sys.argv[2]


    # 是否立即验证
    validate_immediately = True
    if len(sys.argv) >= 4:
        validate_immediately = sys.argv[3].lower() == "true"
    
    # 解决任务

    solution_path = solve_mbpp_task_zero_shot(task_id, dataset_path, validate_immediately)
    
    if solution_path:
        print(f"\n任务 {task_id} 已完成！")
        if not validate_immediately:
            print(f"你可以使用以下命令测试解答:")
            print(f"python mbpp_tester_from_file.py {solution_path} {task_id}")



if __name__ == "__main__":
    main()