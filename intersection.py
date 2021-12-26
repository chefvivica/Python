def intersection(a, b):
  set_a = set(a)
  
  return [i for i in b if i in set_a]


#set look up O(1)