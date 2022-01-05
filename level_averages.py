class Node:
  def __init__(self, val):
    self.val = val
    self.left = None
    self.right = None


from statistics import mean

def level_averages(root):
  result = []
  fill_levels(root, result, 0)
  avgs = []
  for item in result:
    avgs.append(mean(item))
    
  return avgs


def fill_levels(root, result, level_num):
  if root is None:
    return
  
  if level_num == len(result):
    result.append([root.val])
  else:
    result[level_num].append(root.val)
    
  fill_levels(root.left, result, level_num + 1)
  fill_levels(root.right, result, level_num + 1)
    



