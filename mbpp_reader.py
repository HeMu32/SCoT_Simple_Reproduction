import json
import sys
from typing import Dict, Any, Optional

def read_jsonl_record(file_path: str, record_index: int = 0) -> Optional[Dict[str, Any]]:
    """
    从JSONL文件中读取指定索引的记录
    
    Args:
        file_path: JSONL文件路径
        record_index: 要读取的记录索引（从0开始）
        
    Returns:
        记录的字典表示，如果索引无效则返回None
    """
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            for i, line in enumerate(f):
                if i == record_index:
                    return json.loads(line.strip())
        print(f"错误：索引 {record_index} 超出文件范围")
        return None
    except Exception as e:
        print(f"读取文件时出错: {e}")
        return None

def format_record(record: Dict[str, Any]) -> str:
    """
    格式化MBPP记录为可读的字符串
    
    Args:
        record: MBPP记录的字典表示
        
    Returns:
        格式化后的字符串
    """
    if not record:
        return "无效记录"
    
    formatted = []
    formatted.append("=" * 50)
    formatted.append(f"任务ID: {record.get('task_id', 'N/A')}")
    formatted.append("=" * 50)
    
    formatted.append("\n## 问题描述")
    formatted.append(record.get('text', 'N/A'))
    
    formatted.append("\n## 解决方案代码")
    formatted.append("```python")
    formatted.append(record.get('code', 'N/A'))
    formatted.append("```")
    
    formatted.append("\n## 测试用例")
    for i, test in enumerate(record.get('test_list', []), 1):
        formatted.append(f"{i}. {test}")
    
    if record.get('test_setup_code'):
        formatted.append("\n## 测试设置代码")
        formatted.append("```python")
        formatted.append(record.get('test_setup_code'))
        formatted.append("```")
    
    if record.get('challenge_test_list'):
        formatted.append("\n## 挑战测试")
        for i, test in enumerate(record.get('challenge_test_list', []), 1):
            formatted.append(f"{i}. {test}")
    
    return "\n".join(formatted)

def main():
    """主函数"""
    if len(sys.argv) < 2:
        file_path = "c:\\Users\\HeMu\\Desktop\\SCoT-Rep\\mbpp.jsonl"  # 默认文件路径
    else:
        file_path = sys.argv[1]
    
    record_index = 0
    if len(sys.argv) >= 3:
        try:
            record_index = int(sys.argv[2])
        except ValueError:
            print("错误：记录索引必须是整数")
            return
    
    record = read_jsonl_record(file_path, record_index)
    if record:
        formatted_record = format_record(record)
        print(formatted_record)
        
        # 可选：将格式化后的记录保存到文件
        # output_file = f"mbpp_record_{record.get('task_id', record_index)}.md"
        # with open(output_file, 'w', encoding='utf-8') as f:
        #     f.write(formatted_record)
        # print(f"\n格式化后的记录已保存到 {output_file}")

if __name__ == "__main__":
    main()