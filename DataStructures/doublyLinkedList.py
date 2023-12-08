class DoublyLinkedList:
    def __init__(self, data, next=None, prev=None):
        self.data = data
        self.next = next
        self.prev = prev


def print_doubly_linked_list_forward(node):
    while node:
        print(node.data, end=" <-> ")
        node = node.next
    print(None)


def print_doubly_linked_list_backward(node):
    while node and node.next:
        node = node.next
    while node:
        print(node.data, end=" <-> ")
        node = node.prev
    print(None)


doublyLinkedList = DoublyLinkedList(0)
doublyLinkedList.next = DoublyLinkedList(1)
doublyLinkedList.next.prev = doublyLinkedList
doublyLinkedList.next.next = DoublyLinkedList(2)
doublyLinkedList.next.next.prev = doublyLinkedList.next
doublyLinkedList.next.next.next = DoublyLinkedList(3)
doublyLinkedList.next.next.next.prev = doublyLinkedList.next.next

print("Forward:")
print_doubly_linked_list_forward(doublyLinkedList)

print("\nBackward:")
print_doubly_linked_list_backward(doublyLinkedList)
