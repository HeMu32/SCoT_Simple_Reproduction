def No_of_Triangle(N, K):
  # Calculate the number of smaller triangles that can fit along one side
  num_fit = N // K
  # The total number of smaller triangles that can fit within the larger one
  count = num_fit ** 2
  return count