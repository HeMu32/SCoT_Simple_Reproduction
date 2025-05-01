import re

def text_match_two_three(text):
    pattern = 'ab{2,3}'
    match = re.search(pattern, text)
    if match:
        return True
    else:
        return False