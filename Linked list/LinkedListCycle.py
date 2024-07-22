class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def hasCycle(head: ListNode) -> bool:
    if not head or not head.next:
        return False

    slow = head
    fast = head.next

    while slow != fast:
        if not fast or not fast.next:
            return False
        slow = slow.next
        fast = fast.next.next

    return True

# Helper function to create a linked list with a cycle for testing
def createLinkedListWithCycle(values, pos):
    if not values:
        return None
    head = ListNode(values[0])
    current = head
    cycle_node = None

    if pos == 0:
        cycle_node = head

    for i in range(1, len(values)):
        current.next = ListNode(values[i])
        current = current.next
        if i == pos:
            cycle_node = current

    if cycle_node:
        current.next = cycle_node

    return head


if __name__ == "__main__":
    
    list_values=list(map(int, input().split()))
    pos=int(input())
    head = createLinkedListWithCycle([3, 2, 0, -4], 1)
    print( hasCycle(head))
