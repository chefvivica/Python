class Node:
  def __init__(self, val):
    self.val = val
    self.left = None
    self.right = None

def how_high(node):
  if node is None:
    return -1
 
  left_tree = how_high(node.left)
  right_tree = how_high(node.right)
  
  return 1 + max(left_tree, right_tree)