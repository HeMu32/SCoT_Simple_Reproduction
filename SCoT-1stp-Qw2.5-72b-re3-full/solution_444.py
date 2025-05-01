def trim_tuple(test_list, K):
  result = []
  for tup in test_list:
    if len(tup) > 2 * K:
      trimmed_tup = tup[K:-K]
      result.append(trimmed_tup)
  return result