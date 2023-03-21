

def has_loop(head):
    """
    Checks if the given linked list has a loop.

    Args:
        head (Node): The head of the linked list.

    Returns:
        bool: True if the linked list has a loop, False otherwise.
    """
    slow = head
    fast = head

    while fast is not None and fast.next is not None:
        slow = slow.next
        fast = fast.next.next

        if slow == fast:
            return True

    return False