from collections import Counter

def freq_element(nums):
    elements = []
    for sublist in nums:
        elements.extend(sublist)
    freq = dict(Counter(elements))
    return freq