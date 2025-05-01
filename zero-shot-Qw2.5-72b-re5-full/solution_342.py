import heapq

def smallest_range(lists):
    min_heap = []
    current_max = float('-inf')
    
    # Initialize the heap with the first element of each list along with the list index and element index
    for i in range(len(lists)):
        heapq.heappush(min_heap, (lists[i][0], i, 0))
        current_max = max(current_max, lists[i][0])
    
    result = (-float('inf'), float('inf'))
    
    while min_heap:
        current_min, list_idx, element_idx = heapq.heappop(min_heap)
        
        if current_max - current_min < result[1] - result[0]:
            result = (current_min, current_max)
        
        if element_idx + 1 < len(lists[list_idx]):
            next_element = lists[list_idx][element_idx + 1]
            heapq.heappush(min_heap, (next_element, list_idx, element_idx + 1))
            current_max = max(current_max, next_element)
        else:
            break
    
    return result

class Solution:
    def __init__(self, value, list_num, index):
        self.value = value
        self.list_num = list_num
        self.index = index
        self.range = smallest_range(self.list_num)