def insert_node(head, value, index):
  new_head = Node(value)
  if index == 0:
    new_head.next = head
    return new_head

  count = 1
  current = head
  prev = None
  while current is not None:
    if count == index:
      nextNode = current.next
      current.next = new_head
      current.next.next = nextNode

    current = current.next
    count += 1

  return head