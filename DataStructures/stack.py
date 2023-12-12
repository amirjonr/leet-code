# last input first output
class Stack:
    def __init__(self):
        self.items = []

    def is_empty(self):
        return len(self.items) == 0

    def push(self, item):
        self.items.append(item)

    def pop(self):
        if not self.is_empty():
            return self.items.pop()
        else:
            raise IndexError("pop from an empty stack")

    def peek(self):
        if not self.is_empty():
            return self.items[-1]
        else:
            raise IndexError("peek from an empty stack")

    def size(self):
        return len(self.items)


my_stack = Stack()

my_stack.push(1)
my_stack.push(2)
my_stack.push(3)

print("Top element:", my_stack.peek())

print("Pop:", my_stack.pop())
print("Pop:", my_stack.pop())

print("Stack size:", my_stack.size())


# ----------------------------- Advantages -----------------------------------------------------------------------#
# Stacks are simple data structures with a well-defined set of operations, which makes them easy to understand and
# use. Stacks are efficient for adding and removing elements, as these operations have a time complexity of O(1). In
# order to reverse the order of elements we use the stack data structure.
# -------------------------------- Disadvantages ------------------------------------------------------------#
# Stacks do not provide fast access to elements other than the top element. Stacks do not support efficient
# searching, as you have to pop elements one by one until you find the element you are looking for.

# Examples of stack use:
# Stacks can be used to implement undo/redo
