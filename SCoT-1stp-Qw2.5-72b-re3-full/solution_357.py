def find_max(test_list):
  max_value = float('-inf')  # Initialize max_value to negative infinity
  for tup in test_list:
    for elem in tup:
      if elem > max_value:
        max_value = elem
  return max_value