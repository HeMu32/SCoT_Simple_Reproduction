import heapq

def find_minimum_range(lists):
    # Initialize the heap and the variables to track the current and overall minimum range
    heap = []
    current_max = float('-inf')
    overall_min_range = float('inf')
    start = 0
    end = 0

    # Initialize the heap with the first element of each list
    for i, lst in enumerate(lists):
        heapq.heappush(heap, (lst[0], i, 0))
        current_max = max(current_max, lst[0])

    # Process the heap until we have considered all elements
    while heap:
        current_min, list_idx, element_idx = heapq.heappop(heap)

        # Update the overall minimum range if the current range is smaller
        if current_max - current_min < overall_min_range:
            overall_min_range = current_max - current_min
            start = current_min
            end = current_max

        # If there are more elements in the current list, push the next element into the heap
        if element_idx + 1 < len(lists[list_idx]):
            next_element = lists[list_idx][element_idx + 1]
            heapq.heappush(heap, (next_element, list_idx, element_idx + 1))
            current_max = max(current_max, next_element)
        else:
            # If any list is exhausted, we cannot form a range with all lists
            break

    return (start, end)