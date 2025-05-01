def is_valid_parenthese(str1):
    stack = []
    parentheses_map = {')': '(', '}': '{', ']': '['}
    
    for char in str1:
        if char in parentheses_map.values():
            stack.append(char)
        elif char in parentheses_map.keys():
            if not stack or stack.pop() != parentheses_map[char]:
                return False
    return not stack