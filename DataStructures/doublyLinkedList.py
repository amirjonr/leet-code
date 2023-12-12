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


def insert_at_beginning(head, data):
    new_node = DoublyLinkedList(data)
    new_node.next = head
    if head:
        head.prev = new_node
    return new_node


def insert_in_middle(head, data, position):
    new_node = DoublyLinkedList(data)

    if position == 0:
        return insert_at_beginning(head, data)

    current = head
    count = 0

    while current and count < position - 1:
        current = current.next
        count += 1

    if not current:
        print("Недопустимая позиция. Вставка в конец.")
        return insert_at_end(head, data)

    new_node.next = current.next
    new_node.prev = current
    if current.next:
        current.next.prev = new_node
    current.next = new_node

    return head


def insert_at_end(head, data):
    new_node = DoublyLinkedList(data)
    if not head:
        return new_node

    current = head
    while current.next:
        current = current.next

    current.next = new_node
    new_node.prev = current
    return head


def delete_by_value(head, value):
    current = head
    while current and current.data != value:
        current = current.next

    if current:
        if current.prev:
            current.prev.next = current.next
        if current.next:
            current.next.prev = current.prev
        if current == head:
            head = current.next

    return head


# Example usage:
doublyLinkedList = DoublyLinkedList(0)
doublyLinkedList.next = DoublyLinkedList(1)
doublyLinkedList.next.prev = doublyLinkedList
doublyLinkedList.next.next = DoublyLinkedList(2)
doublyLinkedList.next.next.prev = doublyLinkedList.next
doublyLinkedList.next.next.next = DoublyLinkedList(3)
doublyLinkedList.next.next.next.prev = doublyLinkedList.next.next

print("Original Doubly Linked List:")
print_doubly_linked_list_forward(doublyLinkedList)

# Insert at the beginning
doublyLinkedList = insert_at_beginning(doublyLinkedList, -1)
print("\nDoubly Linked List after inserting at the beginning:")
print_doubly_linked_list_forward(doublyLinkedList)

# Insert at the end
doublyLinkedList = insert_at_end(doublyLinkedList, 4)
print("\nDoubly Linked List after inserting at the end:")
print_doubly_linked_list_forward(doublyLinkedList)

# Delete by value
doublyLinkedList = delete_by_value(doublyLinkedList, 2)
print("\nDoubly Linked List after deleting node with value 2:")
print_doubly_linked_list_forward(doublyLinkedList)

position_to_insert = 2
data_to_insert = 100
head = insert_in_middle(doublyLinkedList, data_to_insert, position_to_insert)

print("\nAfter inserting in the middle:")
print_doubly_linked_list_backward(head)

# example of use
# navigations
