class Node:
  def __init__(self, val):
    self.val = val
    self.left = None
    self.right = None

def all_tree_paths(root):
  if root is None:
    return []
  if root.left is None and root.right is None:
    return [[root.val]]
  
  result = []
  left_tree = all_tree_paths(root.left)
  for item in left_tree:
    result.append([root.val] +item)
  
  right_tree = all_tree_paths(root.right)
  for item in right_tree:
    result.append([root.val] +item)
    
  return result