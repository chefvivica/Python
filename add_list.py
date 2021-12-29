#solution1
class Node:
  def __init__(self, val):
    self.val = val
    self.next = None

def add_lists(head_1, head_2):
  
  num_1 = 0 
  current_1 = head_1
  while current_1 is not None:
    num_1 = num_1 * 10 + current_1.val
    current_1= current_1.next
  
  num_1 = int(str(num_1)[::-1])
  num_2 = 0 
  current_2 = head_2
  while current_2 is not None:
    num_2 = num_2 * 10 + current_2.val
    current_2= current_2.next
  num_2 = int(str(num_2)[::-1])
  sum  = str(num_1 + num_2)
  reverse_sum = str(sum)[::-1]
  
  head = Node(reverse_sum[0])
  tail = head
  i = 1
  while i < len(reverse_sum):
    nextNode = Node(int(reverse_sum[i]))
    tail.next = nextNode
    tail = tail.next
    i += 1
  return head

# recursive solution
def add_lists_1(head_1, head_2, carry = 0):
  
  if head_1 is None and head_2 is None and carry == 0:
    return None
  val_1 = 0 if head_1 is None else head_1.val
  val_2 = 0 if head_2 is None else head_2.val

  sum = val_1 + val_2 + carry
  next_carry = 1 if sum > 9 else 0
  digit = sum % 10
  result = Node(digit)
  next_1 = None if head_1 is None else head_1.next
  next_2 = None if head_2 is None else head_2.next
  result.next = add_lists(next_1, next_2, next_carry)
  return result
