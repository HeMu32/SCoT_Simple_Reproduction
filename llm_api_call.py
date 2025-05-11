from openai import OpenAI
import time
import re
import os
from typing import Dict, Any, List

# 导入测试相关函数
from mbpp_tester_from_file import run_test, generate_test_report

from config import API_KEY, BASE_URL, MODEL_NAME, MAX_TOKENS, TIMEOUT, TEMPERATURE, MAX_RETRIES, RETRY_DELAY  # 导入所有配置参数

# 设置API密钥和基础URL
client = OpenAI(
    api_key=API_KEY,  # 从配置文件读取API密钥
    base_url=BASE_URL,  # 从配置文件读取基础URL
    timeout=TIMEOUT  # 从配置文件读取超时设置
)

def is_valid_response(response: str) -> bool:
    """
    检查API返回的响应是否有效
    
    参数:
        response (str): API返回的响应文本
        
    返回:
        bool: 如果响应有效返回True，否则返回False
    """
    # 检查是否包含HTML错误页面的特征
    if re.search(r'<!DOCTYPE html>', response, re.IGNORECASE) or \
       re.search(r'<html', response, re.IGNORECASE) or \
       re.search(r'<body', response, re.IGNORECASE) or \
       re.search(r'Error code \d+', response):
        return False
    
    # 检查是否包含常见的错误信息
    error_patterns = [
        r'timeout occurred', 
        r'error \d+',
        r'cloudflare',
        r'请求超时',
        r'服务器错误',
        r'524: A timeout occurred',  # 添加Cloudflare特定的超时错误
        r'524 error',
        r'cloudflare timeout',
        r'timed out',
        r'connection timed out'
    ]
    
    for pattern in error_patterns:
        if re.search(pattern, response, re.IGNORECASE):
            return False
    
    return True

def call_llm(prompt, conversation_history=None, max_tokens=None, max_retries=None, retry_delay=None):
    """
    调用DeepSeek-V3模型并获取回复，支持自动重试
    
    参数:
        prompt (str): 输入提示文本
        conversation_history (list): 对话历史记录
        max_tokens (int): 生成的最大token数量
        max_retries (int): 最大重试次数
        retry_delay (int): 重试间隔时间（秒）
        
    返回:
        str: 模型生成的回复文本
        list: 更新后的对话历史
    """
    # 如果没有提供对话历史，则初始化一个空列表
    if conversation_history is None:
        conversation_history = []
    
    # 使用配置文件中的默认值
    if max_tokens is None:
        max_tokens = MAX_TOKENS
    
    if max_retries is None:
        max_retries = MAX_RETRIES
        
    if retry_delay is None:
        retry_delay = RETRY_DELAY
    
    # 将当前用户输入添加到对话历史
    conversation_history.append({"role": "user", "content": prompt})
    
    retry_count = 0
    last_error = None
    
    while retry_count <= max_retries:
        try:
            if retry_count > 0:
                print(f"第 {retry_count} 次重试，等待 {retry_delay} 秒...")
                time.sleep(retry_delay)
            
            print("正在发送请求到API...")
            start_time = time.time()
            
            # 创建聊天完成请求，传入完整的对话历史
            response = client.chat.completions.create(  # 使用client实例而不是openai
                model=MODEL_NAME,  # 从配置文件读取模型名称
                messages=conversation_history,
                max_tokens=max_tokens,
                temperature=TEMPERATURE,  # 从配置文件读取温度参数
            )
            
            elapsed_time = time.time() - start_time
            print(f"请求完成，耗时: {elapsed_time:.2f}秒")
            
            # 提取回复文本
            reply = response.choices[0].message.content
            
            # 检查响应是否有效
            if not is_valid_response(reply):
                raise Exception("API返回了无效的响应（可能是HTML错误页面）")
            
            # 将模型回复添加到对话历史
            conversation_history.append({"role": "assistant", "content": reply})
            
            return reply, conversation_history
            
        except Exception as e:
            last_error = e
            retry_count += 1
            print(f"API调用出错: {str(e)}")
            
            # 如果已经达到最大重试次数，则抛出最后一个错误
            if retry_count > max_retries:
                print(f"达到最大重试次数 {max_retries}，放弃请求")
                # 返回一个错误消息作为回复
                error_message = f"调用API时出错: {str(e)}"
                # 将错误消息添加到对话历史
                conversation_history.append({"role": "assistant", "content": error_message})
                return error_message, conversation_history
    
    # 这行代码理论上不会执行到，但为了代码完整性添加
    return f"调用API时出错: {str(last_error)}", conversation_history


def clear_conversation_history():
    """

    清除对话历史，开启新话题
    

    返回:

        list: 空的对话历史列表
    """

    print("已清除对话历史，开启新话题")

    return []


def validate_solution(solution_path: str, task_id: int, task: Dict[str, Any], result_dir: str = "./ans_cache/", result_filename: str = "test_results.json", timeout: int = 10):
    """
    验证解答是否通过所有测试用例
    
    Args:
        solution_path: 解答文件路径
        task_id: 任务ID
        task: 任务数据
        result_dir: 结果保存目录，默认为"./ans_cache/"
        result_filename: 结果文件名，默认为"test_results.json"
        timeout: 测试超时时间（秒），默认为10秒
    """
    # 初始化测试结果列表
    test_results = []
    test_passed_list = []  # 记录每个测试用例是否通过
    error_messages = []    # 记录每个测试用例的错误信息
    
    try:
        # 读取解答代码
        with open(solution_path, 'r', encoding='utf-8') as f:
            code = f.read()
        
        # 获取测试用例
        test_cases = task.get('test_list', [])
        
        # 运行测试
        for i, test_case in enumerate(test_cases):
            passed, error = run_test(code, test_case, timeout)
            test_results.append({
                'test_case': test_case,
                'passed': passed,
                'error': error
            })
            test_passed_list.append(passed)  # 记录测试结果
            
            # 记录错误信息，确保即使是空错误也有记录
            if not passed:
                error_message = error if error else "Assertion failed"
                error_messages.append(error_message)
                print(f"测试 {i+1}: ❌ 失败")
                print(f"  错误: {error_message}")
            else:
                error_messages.append("")
                print(f"测试 {i+1}: ✅ 通过")
        
        # 生成测试报告
        passed_count = sum(1 for result in test_results if result['passed'])
        total_count = len(test_results)
        print(f"\n测试总结: 通过 {passed_count}/{total_count} 测试用例")
        
        # 更新测试结果JSON文件
        json_path = os.path.join(result_dir, result_filename)
        try:
            update_test_results_json(task_id, test_passed_list, json_path, error_messages)
            print(f"测试结果已保存到: {json_path}")
        except Exception as e:
            print(f"保存测试结果时出错: {e}")
    
    except Exception as e:
        print(f"验证解答时出错: {e}")
        return False
    
    # 返回是否所有测试都通过
    return all(test_passed_list)

def ensure_directory_exists(directory_path: str):
    """确保目录存在，如果不存在则创建"""
    if not os.path.exists(directory_path):
        os.makedirs(directory_path)

def update_test_results_json(task_id: int, test_passed_list: list, json_path: str = "./ans_cache/test_results.json", error_messages: list = None):
    """
    更新测试结果JSON文件，保存每次测试的结果历史
    
    Args:
        task_id: 任务ID
        test_passed_list: 测试通过情况列表
        json_path: JSON文件路径
        error_messages: 测试错误信息列表
    """
    # 确保导入必要的模块
    import os
    import json
    
    # 确保目录存在
    ensure_directory_exists(os.path.dirname(json_path))
    
    # 读取现有的JSON文件（如果存在）
    results_data = {}
    if os.path.exists(json_path):
        try:
            with open(json_path, 'r', encoding='utf-8') as f:
                results_data = json.load(f)
        except json.JSONDecodeError:
            # 如果文件存在但不是有效的JSON，创建一个新的空字典
            results_data = {}
        except Exception as e:
            print(f"读取测试结果文件时出错: {e}")
            results_data = {}
    
    # 添加或更新当前任务的测试结果
    task_id_str = str(task_id)
    
    # 如果任务ID不存在，创建新记录
    if task_id_str not in results_data:
        results_data[task_id_str] = {
            "total_tests": 0,
            "history": []
        }
    
    # 更新测试次数
    results_data[task_id_str]["total_tests"] += 1
    current_test_number = results_data[task_id_str]["total_tests"]
    
    # 创建新的测试记录
    new_test_record = [current_test_number] + test_passed_list
    
    # 添加错误信息到测试记录
    if error_messages:
        # 提取错误信息的主要部分，转换为英文
        simplified_errors = []
        for error in error_messages:
            if error:
                # 提取错误信息的核心部分并转换为英文
                if "执行错误:" in error:
                    simplified_errors.append("Execution error: " + error.split("执行错误:")[1].strip())
                elif "断言错误:" in error:
                    simplified_errors.append("Assertion error: " + (error.split("断言错误:")[1].strip() or "Assertion failed"))
                elif "断言错误" in error:
                    simplified_errors.append("Assertion error: Assertion failed")
                else:
                    # 如果是其他类型的错误，直接使用英文描述
                    simplified_errors.append("Error: " + error)
            else:
                simplified_errors.append("")
        
        # 将错误信息添加到测试记录中
        new_test_record.extend(simplified_errors)
    else:
        # 如果没有提供错误信息，但有测试失败的情况，添加默认错误信息
        if not all(test_passed_list):
            default_errors = []
            for passed in test_passed_list:
                if not passed:
                    default_errors.append("Unknown error")
                else:
                    default_errors.append("")
            new_test_record.extend(default_errors)
        else:
            # 如果所有测试都通过，添加空字符串
            new_test_record.extend(["" for _ in test_passed_list])
    
    # 添加到历史记录
    results_data[task_id_str]["history"].append(new_test_record)
    
    # 保存更新后的JSON文件
    try:
        with open(json_path, 'w', encoding='utf-8') as f:
            json.dump(results_data, f, indent=2)
    except Exception as e:
        print(f"保存测试结果文件时出错: {e}")
    
    return json_path


if __name__ == "__main__":

    # 初始化对话历史

    conversation_history = []
    

    # 示例使用 - 第一轮对话

    user_prompt = "请简要介绍一下人工智能的发展历史"

    response_text, conversation_history = call_llm(user_prompt, conversation_history)
    

    print("用户提问:", user_prompt)

    print("\n回复内容:")

    print(response_text)
    

    # 示例使用 - 第二轮对话（引用上下文）

    user_prompt2 = "简短概况你刚才的回复. "

    response_text2, conversation_history = call_llm(user_prompt2, conversation_history)
    

    print("\n\n用户提问:", user_prompt2)

    print("\n回复内容:")

    print(response_text2)
    

    # 示例 - 清除对话历史，开启新话题

    conversation_history = clear_conversation_history()
    

    # 开始新话题

    user_prompt3 = "什么是机器学习？"

    response_text3, conversation_history = call_llm(user_prompt3, conversation_history)
    

    print("\n\n新话题")

    print("用户提问:", user_prompt3)

    print("\n回复内容:")

    print(response_text3)