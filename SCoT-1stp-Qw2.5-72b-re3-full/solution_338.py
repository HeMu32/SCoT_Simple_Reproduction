def count_Substring_With_Equal_Ends(s):
  count = 0
  for i in range(len(s)):
    for j in range(i, len(s)):
      substring = s[i:j+1]
      if substring[0] == substring[-1]:
        count += 1
  return count