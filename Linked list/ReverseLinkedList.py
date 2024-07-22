class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def reverseList(head: ListNode) -> ListNode:
    prev = None
    current = head
    
    while current:
        next_node = current.next  # Store the next node
        current.next = prev       # Reverse the current node's pointer
        prev = current            # Move prev to this node
        current = next_node       # Move to the next node
    
    return prev

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
    head1 = createList(list(map(int,input().split())))
    #printList(head1)
    reversed_head1 = reverseList(head1)
    #print("Reversed List 1:")
    printList(reversed_head1)
