from collections import deque
def breadth_first_values(root):
  if root is None:
    return []
  queue = deque([ root ])
  result = [ ]
  while queue:
    current = queue.popleft()
    result.append(current.val)
    if current.left is not None and current.right is not None:
      queue.append(current.left)
      queue.append(current.right)
    if current.left is not None and current.right is None:
      queue.append(current.left)
    if current.right is not None and current.left is None:
      queue.append(current.right)
  return result
  