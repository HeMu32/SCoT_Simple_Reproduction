def add_tuples(t1, t2):
  """Helper function to add two tuples element-wise."""
  return tuple(a + b for a, b in zip(t1, t2))

def add_nested_tuples(test_tup1, test_tup2):
  """Function to perform index-wise addition of tuple elements in the given two nested tuples."""
  
  def add_nested(t1, t2):
    """Recursive function to handle nested tuples."""
    if isinstance(t1, tuple) and isinstance(t2, tuple):
      return add_tuples(t1, t2)
    else:
      return t1 + t2
  
  # Using a recursive approach to handle nested structures
  return add_nested(test_tup1, test_tup2)