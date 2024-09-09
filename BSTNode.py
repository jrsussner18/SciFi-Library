# Jake Sussner
# Binary Search Tree Node file


class BSTNode:
    def __init__(self, name=None, author=None, checked=None, priority=None, l=None, r=None):
        # instead of just having data, storing each part of the book in a separate part of the node makes it easier to access those pieces of data
        self.name = name
        self.author = author
        self.checked = checked
        self.priority = priority
        self._left = l
        self._right = r

    @property
    def left(self):
        return self._left

    @left.setter
    def left(self, l):
        self._left = l

    @property
    def right(self):
        return self._right

    @right.setter
    def right(self, r):
        self._right = r

    def __str__(self):
        return f"Name: {self.name}, Author: {self.author}, Checked: {"In" if self.checked == 1 else "Out"}, Priority: {self.priority}\n"
