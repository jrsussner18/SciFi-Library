# Jake Sussner
# Stack file

from BSTNode import BSTNode


# Stack class
class Stack:
    def __init__(self):
        self._items = []

    # checks if stack is empty
    def isEmpty(self):
        return len(self._items) == 0

    # adds node to stack
    def push(self, item):
        self._items.append(item)

    # deletes the node on top of the stack
    def pop(self):
        if self.isEmpty():
            raise IndexError("pop from an empty stack")
        return self._items.pop()

    # outputs the current node on top of the stack
    def peek(self):
        if self.isEmpty():
            raise IndexError("peek from an emtpy stack")
        return self._items[-1]

    # finds the stack size
    def size(self):
        return len(self._items)
