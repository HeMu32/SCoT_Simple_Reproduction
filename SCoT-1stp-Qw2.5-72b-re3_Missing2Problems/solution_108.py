import heapq

def merge_sorted_list(num1, num2, num3):
    # Initialize the heap
    heap = []
    
    # Function to push the first element of each list into the heap
    def push_initial_elements():
        for index, lst in enumerate((num1, num2, num3)):
            if lst:  # Check if the list is not empty
                heapq.heappush(heap, (lst[0], index, 0))
    
    push_initial_elements()
    
    # Merge the lists
    while heap:
        value, list_index, element_index = heapq.heappop(heap)
        yield value
        if element_index + 1 < len((num1, num2, num3)[list_index]):
            next_value = (num1, num2, num3)[list_index][element_index + 1]
            heapq.heappush(heap, (next_value, list_index, element_index + 1))