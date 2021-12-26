def most_frequent_char(s):
  count= {}
  for i in s:
    if i not in count:
      count[i] = 0
    count[i] += 1
    
  best = None;
  
  for i in s:
    if best is None or count[i] > count[best]:
      best = i
  return best



print(most_frequent_char


('mississippi'))