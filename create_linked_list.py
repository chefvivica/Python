def create_linked_list(values):
  if len(values) == 0:
    return None
  head_node = Node(values[0])
  current = head_node
  i = 1
  while i < len(values):
    next_node = Node(values[i])
    current.next = next_node
    current = current.next
    i += 1
  return head_node
