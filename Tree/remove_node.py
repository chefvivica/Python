def remove_node(head, target_val):
  if head.val == target_val:
    return head.next
  prev = head
  current = head.next
  while current is not None:
    if current.val != target_val:
      prev = current
      current = current.next
    else:
      next = current.next
      prev.next = next
      break
  return head