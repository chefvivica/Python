# class Node:
#   def __init__(self, val):
#     self.val = val
#     self.left = None
#     self.right = None

from collections import deque
def breadth_first_values(root):
    if root is None:
        return []
    queue = deque([ root ])
    result = [ ]
    while queue:
        current = queue.popleft()
        result.append(current.val)
        if current.left:
            queue.append(current.left)

        if current.right:
            queue.append(current.right)
    return result
  