
def has_loop(list_head):
    """Check if a linked list contains a loop.

    Parameters:
    list_head (Node): Head of the linked list

    Returns:
    bool: True if the linked list contains a loop, False otherwise
    """
    slow_ptr = list_head
    fast_ptr = list_head

    while fast_ptr and fast_ptr.next:
        slow_ptr = slow_ptr.next
        fast_ptr = fast_ptr.next.next
        if slow_ptr == fast_ptr:
            return True
    return False