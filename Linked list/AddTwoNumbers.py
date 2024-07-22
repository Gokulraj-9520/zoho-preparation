class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def addTwoNumbers(l1: ListNode, l2: ListNode) -> ListNode:
    dummy_head = ListNode(0)
    current = dummy_head
    carry = 0

    while l1 or l2 or carry:
        val1 = l1.val if l1 else 0
        val2 = l2.val if l2 else 0
        total = val1 + val2 + carry
        carry = total // 10
        current.next = ListNode(total % 10)
        current = current.next

        if l1:
            l1 = l1.next
        if l2:
            l2 = l2.next

    return dummy_head.next

def createList(values: list) -> ListNode:
    if not values:
        return None
    head = ListNode(values[0])
    current = head
    for value in values[1:]:
        current.next = ListNode(value)
        current = current.next
    return head

def printList(head: ListNode) -> None:
    current = head
    while current:
        print(current.val, end=" ")
        current = current.next
    print()


if __name__ == "__main__":
    l1_value=list(map(int,input().split()))
    l1 = createList(l1_value)
    l2_value=list(map(int,input().split()))
    l2 = createList(l2_value)
    #print("List 1:")
    #printList(l1)
    #print("List 2:")
    #printList(l2)
    result = addTwoNumbers(l1, l2)
    #print("Sum List:")
    printList(result)

