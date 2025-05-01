import re

def find_adverb_position(text):
    """
    Write a function to find all adverbs and their positions in a given sentence.
    """
    adverbs = re.finditer(r'\b\w+ly\b', text)
    return [(match.group(), match.start()) for match in adverbs]

# Example usage:
# text = "He quickly ran to the store and bought some food."
# print(find_adverb_position(text))
# Output: [('quickly', 3), ('quickly', 28)]