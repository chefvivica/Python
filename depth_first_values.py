# class Node:
#   def __init__(self, val):
#     self.val = val
#     self.left = None
#     self.right = None

def depth_first_values(root):
  if root is None:
    return []
  stack = [ root ]
  result = []
  
  while stack: 
    current = stack.pop()
    result.append(current.val)
    if current.right is not None:
      stack.append(current.right)
    
    if current.left is not None:
      stack.append(current.left)
  return result

