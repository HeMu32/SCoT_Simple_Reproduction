def extract_singly(test_list):
  # Initialize a dictionary to store the frequency of each element
  freq_dict = {}
  
  # Iterate over each tuple in the list
  for tup in test_list:
    # Iterate over each element in the tuple
    for ele in tup:
      # If the element is not in the dictionary, add it with a count of 1
      if ele not in freq_dict:
        freq_dict[ele] = 1
      # If the element is already in the dictionary, increment its count
      else:
        freq_dict[ele] += 1
  
  # Initialize a list to store elements that occur exactly once
  res = []
  
  # Iterate over the dictionary to find elements that occur exactly once
  for k, v in freq_dict.items():
    if v == 1:
      res.append(k)
  
  # Return the list of elements that occur exactly once
  return res