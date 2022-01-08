def longest_streak(head):
  prev_val = None
  current_streak = 0
  max_streak = 0
  current = head
  while current is not None:
    if current.val == prev_val:
      current_streak += 1
    else:
      current_streak = 1
    prev_val = current.val
    current = current.next
    
    if max_streak < current_streak:
      max_streak = current_streak
  return max_streak

