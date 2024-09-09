# Jake Sussner
# Heap file

from BSTNode import BSTNode


# Max Heap Class (based on the priority value of the books)
class Heap:
    def __init__(self):
        self.heap = []

    # check if the heap is empty
    def isEmpty(self):
        return len(self.heap) == 0

    # add a node to the heap
    def push(self, node):
        self.heap.append(node)
        # maintain heap property after insert
        self.heapifyUp(len(self.heap) - 1)

    # delete the maximum node from the heap
    def pop(self):
        if self.isEmpty():
            raise IndexError("Heap is empty")
        self.swap(0, len(self.heap) - 1)
        removed = self.heap.pop()
        # maintain heap property after removal
        self.heapifyDown(0)
        return removed

    # look at the maximum value of the heap
    def peek(self):
        if self.isEmpty():
            raise IndexError("Heap is empty")
        return self.heap[0]

    # get the index of the parent for a node
    def parent(self, i):
        if i > 0:
            return (i - 1) // 2
        else:
            return None

    # find the index of the left child
    def leftChild(self, i):
        if 2 * i + 1 < len(self.heap):
            return 2 * i + 1
        else:
            return None

    # find the index of the right child
    def rightChild(self, i):
        if 2 * i + 2 < len(self.heap):
            return 2 * i + 2
        else:
            return None

    # swap nodes in the heap
    def swap(self, i, j):
        self.heap[i], self.heap[j] = self.heap[j], self.heap[i]

    # help maintain heap order when inserting nodes
    def heapifyUp(self, i):
        parent = self.parent(i)
        # makes sure the node with higher priority is always above the lower
        while parent is not None and self.heap[i].priority < self.heap[parent].priority:
            self.swap(i, parent)
            i = parent
            parent = self.parent(i)

    # help maintain heap order when deleting nodes
    def heapifyDown(self, i):
        while True:
            left = self.leftChild(i)
            right = self.rightChild(i)
            smallest = i
            # swaps left child with the current index if it is less than it
            if (
                left is not None
                and self.heap[left].priority < self.heap[smallest].priority
            ):
                smallest = left
            # swaps right child with the current index if it is less than it
            if (
                right is not None
                and self.heap[right].priority < self.heap[smallest].priority
            ):
                smallest = right
            # checks if heap is already in the correct order
            if smallest == i:
                break
            self.swap(i, smallest)
            i = smallest
