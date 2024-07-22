class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def removeNthFromEnd(head: ListNode, n: int) -> ListNode:
    # Create a dummy node which will help simplify edge cases
    dummy = ListNode(0)
    dummy.next = head
    first = dummy
    second = dummy

    # Move first pointer n+1 steps ahead
    for _ in range(n + 1):
        first = first.next
    
    # Move both pointers until first reaches the end
    while first:
        first = first.next
        second = second.next

    # Remove the nth node from the end
    second.next = second.next.next

    # Return the new head
    return dummy.next

def printList(head: ListNode) -> None:
    current = head
    while current:
        print(current.val, end=" ")
        current = current.next
    print()

def createList(values: list) -> ListNode:
    if not values:
        return None
    head = ListNode(values[0])
    current = head
    for value in values[1:]:
        current.next = ListNode(value)
        current = current.next
    return head

# Example Usage:
if __name__ == "__main__":
    # Create linked list from input
    head = createList([1,2,3,4,5])
    n = 2

    # Remove nth node from end
    new_head = removeNthFromEnd(head, n)

    # Print the updated linked list
    print("Updated List:")
    if new_head:
        printList(new_head)
    else:
        print("[]")
