def pair_sum(numbers, target_sum):
  hash = {}
  for index, value in enumerate(numbers):
    diff = target_sum - value
    if diff in hash:
      return (hash[diff], index)
    hash[value] = index
  return -1
  
print(pair_sum([4, 7, 9, 2, 5, 1], 5))