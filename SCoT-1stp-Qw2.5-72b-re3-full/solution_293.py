import math

def otherside_rightangle(w, h):
  # Calculate the square of the hypotenuse
  hypotenuse_squared = w**2 + h**2
  # Compute the length of the hypotenuse
  hypotenuse = math.sqrt(hypotenuse_squared)
  # Return the length of the hypotenuse
  return hypotenuse