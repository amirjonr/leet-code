class LinkedList:
    def __init__(self, value=0, next=None):
        self.value = value
        self.next = next


linked_list = LinkedList(0)
linked_list.next = LinkedList(1)
linked_list.next.next = LinkedList(2)
linked_list.next.next.next = LinkedList(3)


def print_linked_list(node):
    while node:
        print(node.value, end=" -> ")
        node = node.next
    print(None)


print_linked_list(linked_list)
