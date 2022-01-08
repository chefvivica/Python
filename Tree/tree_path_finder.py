class Node:
  def __init__(self, val):
    self.val = val
    self.left = None
    self.right = None

def path_finder(root, target):
  result =  _path_finder(root, target)
  if result is None:
    return None
  else:
    return result[::-1]


def _path_finder(root, target):
  if root is None:
    return None
  if root.val == target:
    return [root.val]
  
  left_tree = _path_finder(root.left, target)
  if left_tree is not None:
    left_tree.append(root.val)
    return left_tree
  
  right_tree = _path_finder(root.right, target)
  if right_tree is not None:
    right_tree.append(root.val)
    return right_tree

  return None