def reverse_list(head):
  prev = None
  current = head
  while current is not None:
    nextNode = current.next
    current.next = prev
    prev = current
    current = nextNode
    
  return prev

#reverse_list(a) # f -> e -> d -> c -> b -> a