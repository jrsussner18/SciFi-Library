# Jake Sussner
# Binary Search Tree file

from BSTNode import BSTNode
from collections import deque


class BST:
    def __init__(self, r=None, c=None):
        self._root = r
        self._curr = c

    @property
    def root(self):
        return self._root

    @root.setter
    def root(self, n):
        self._root = n

    @property
    def curr(self):
        return self._curr

    @curr.setter
    def curr(self, n):
        self._curr = n

    def isEmpty(self):
        if self.root == None:
            return True
        else:
            return False

    def isLeaf(self):
        if self.curr.left == None and self.curr.right == None:
            return True
        else:
            return False

    def getData(self):
        if self.curr == None:
            return None
        else:
            return self.curr.name

    def goRoot(self):
        self.curr = self.root

    def goLeft(self):
        self.curr = self.curr.left

    def goRight(self):
        self.curr = self.curr.right

    def getMin(self):
        self.goRoot()
        while self.curr.left != None:
            self.goLeft()
        return self.getData()

    def getMax(self):
        self.goRoot()
        while self.curr.right != None:
            self.goRight()
        return self.getData()

    # recursive function to insert
    # only used inside binaryTree class!!!
    def insertNode(self, here, n):
        if here == None:
            here = n
        else:
            if n.name < here.name:
                here.left = self.insertNode(here.left, n)
            else:
                here.right = self.insertNode(here.right, n)
        return here

    # inserts a node (n)
    # This is the method you'll call outside of this class
    def insert(self, n):
        if self.isEmpty() == True:
            self.root = n
            self.curr = n
        else:
            self.goRoot()
            self.curr = self.insertNode(self.curr, n)

    # does the actual counting
    # again, used only in-class
    def count(self, n):
        if n == None:
            return 0
        else:
            l = 1
            l += self.count(n.left)
            l += self.count(n.right)
            return l

    # use this outside of the class
    def getSize(self):
        return self.count(self.root)

    # next 2 methods find a node in the tree or returns None if not there
    def findBook(self, n, what):
        if n == None:
            return None  # not found
        if n.name == what:
            return n
        elif what < n.name:
            return self.findBook(n.left, what)
        elif what > n.name:
            return self.findBook(n.right, what)

    def searchBook(self, what):
        self.curr = self.findBook(self.root, what)
        return self.curr

    # remove a node from the tree
    # "what" is the data - use it to find the node to kill
    def remove(self, n, what):
        # base case
        if not n:
            return n

        # recursive calls to find the node to be removed
        if n.name > what:
            n.left = self.remove(n.left, what)
        elif n.name < what:
            n.right = self.remove(n.right, what)

        # node is found
        else:
            # if the node has no left children replace the node with its right child
            if not n.left:
                temp = n.right
                # update the root if necessary
                if n == self.root:
                    self.root = temp
                n = None
                return temp
            # if the node has no right children, replace the node with its left child
            elif not n.right:
                temp = n.left
                # update the root if necessary
                if n == self.root:
                    self.root = temp
                n = None
                return temp

            # if the node has both left and right children, go to the right once, then all the way left
            temp = n.right
            while temp.left is not None:
                temp = temp.left

            # swap the nodes
            n.name = temp.name
            # remove the node that was swapped with temp
            n.right = self.remove(n.right, temp.data)

        # return the current node of binary tree
        return n

    # function called outside of class
    def removeNode(self, what):
        self.goRoot()
        self.remove(self.curr, what)

    ### traversal methods ###
    def inOrder(self, n):
        # prints the nodes in LNR order
        if n is not None:
            self.inOrder(n.left)
            print(n, end=" ")
            self.inOrder(n.right)

    def traverseInOrder(self):
        self.goRoot()
        self.inOrder(self.curr)

    def PreOrder(self, n):
        # prints the nodes in NLR order
        if n is not None:
            print(n, end=" ")
            self.PreOrder(n.left)
            self.PreOrder(n.right)

    def traversePreOrder(self):
        self.goRoot()
        self.PreOrder(self.curr)

    def PostOrder(self, n):
        # prints the nodes in LRN order
        if n is not None:
            self.PostOrder(n.left)
            self.PostOrder(n.right)
            print(n, end=" ")

    def traversePostOrder(self):
        self.goRoot()
        self.PostOrder(self.curr)

    def findAuthorBooks(self, author):
        books = []

        def traverse(node):
            if node is not None:
                if node.author == author:
                    books.append((node.name, node.checked == 1))
                traverse(node.left)
                traverse(node.right)

        traverse(self.root)
        return books

    def booksEndOfDay(self):
        books = []

        def traverse(node):
            if node is not None:
                traverse(node.left)
                books.append((node.name, node.checked == 1))
                traverse(node.right)

        traverse(self.root)
        return books

    # returns a string that when printed
    # shows the tree in tree form
    # for example:
    #         M
    #      F      T
    #    B   H  R   W

    # got the code for this from the CS201ut github page
    # https://github.com/jgourd/CSC201UT/blob/main/CSC201UT/OrderedBinaryTree.py
    def __str__(self):
        return self._str(self.root)

    def _str(self, n, level=0):
        if not n:
            return ""
        return (
            self._str(n.right, level + 1)
            + ("\t" * level + str(n) + "\n")
            + self._str(n.left, level + 1)
        )
