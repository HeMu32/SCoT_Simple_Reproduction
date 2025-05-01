def extract_nth_element(list1, n):
  result = []
  for tup in list1:
    if len(tup) > n:  # Check if the tuple has enough elements
      result.append(tup[n])
  return result