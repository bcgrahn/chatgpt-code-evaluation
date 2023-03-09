

def check_loop(head):
  # Set two pointers, slow and fast
  slow = fast = head
  # Move fast pointer by two nodes
  fast = fast.next
  if fast:
    fast = fast.next
  # Move slow pointer by one node
  slow = slow.next
  # If the two pointers meet, then there is a loop
  while slow != fast:
    # Move fast pointer by two nodes
    fast = fast.next
    if fast:
      fast = fast.next
    # Move slow pointer by one node
    slow = slow.next
    # If the two pointers meet, then there is a loop
    if slow == fast:
      return True
  # If the fast pointer reaches the end, then there is no loop
  return False