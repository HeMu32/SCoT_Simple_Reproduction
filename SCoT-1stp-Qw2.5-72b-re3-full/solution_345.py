def diff_consecutivenums(nums):
  differences = []
  for i in range(len(nums) - 1):
    diff = nums[i + 1] - nums[i]
    differences.append(diff)
  return differences