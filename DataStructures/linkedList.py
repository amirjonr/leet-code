class LinkedList:
    def __init__(self, value=0, next=None):
        self.value = value
        self.next = next

    def insert(self, value):
        new_node = LinkedList(value)
        current = self
        while current.next:
            current = current.next
        current.next = new_node

    def delete(self, value):
        current = self
        if current.value == value:
            return current.next

        while current.next and current.next.value != value:
            current = current.next

        if current.next:
            current.next = current.next.next

        return self

    def search(self, value):
        current = self
        while current:
            if current.value == value:
                return True
            current = current.next
        return False

    def print_linked_list(self):
        current = self
        while current:
            print(current.value, end=" -> ")
            current = current.next
        print(None)


linked_list = LinkedList(0)
linked_list.insert(1)
linked_list.insert(2)
linked_list.insert(3)

linked_list.print_linked_list()

linked_list.delete(2)
linked_list.print_linked_list()
linked_list.search(1)

# example of use:
# music players, navigation in web browsers
