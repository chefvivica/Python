class Node:
  def __init__(self, val):
    self.val = val
    self.left = None
    self.right = None

def tree_value_count(root, target):
  count = 0
  if root is None:
    return 0
  if root.val == target:
    count = 1
  else:
    count = 0
  return  count + tree_value_count(root.right, target) + tree_value_count(root.left, target)