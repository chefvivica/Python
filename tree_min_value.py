class Node:
  def __init__(self, val):
    self.val = val
    self.left = None
    self.right = None

def tree_min_value(root):
  if root is None:
    return float("inf")
  
  smallest_left_value = tree_min_value(root.left)
  smallest_right_value = tree_min_value(root.right)
  
  
  return min(root.val, smallest_left_value, smallest_right_value) 