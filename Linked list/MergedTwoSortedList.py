class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def mergeTwoLists(list1: ListNode, list2: ListNode) -> ListNode:
    dummy = ListNode(0)
    current = dummy

    while list1 and list2:
        if list1.val <= list2.val:
            current.next = list1
            list1 = list1.next
        else:
            current.next = list2
            list2 = list2.next
        current = current.next

    if list1:
        current.next = list1
    elif list2:
        current.next = list2

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
    # Example 1
    list1 = createList(list(map(int,input().split())))
    list2 = createList(list(map(int,input().split())))
    #print("List 1:")
    printList(list1)
    #print("List 2:")
    printList(list2)
    merged_list = mergeTwoLists(list1, list2)
    #print("Merged List:")
    printList(merged_list)