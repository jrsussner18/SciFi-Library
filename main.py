# Jake Sussner
# Final Program
# Science Fiction Library
# 05 - 01 - 2024

# REASONINGS #

# BINARY SEARCH TREE #
# I used a binary search tree with a modified node class for parts 1, 2, and 4. 
# I used it for part 1, which is just grabbing and storing the data, because of its future functionality for some of the other steps. Compared to other data structures like a linked list, it is more efficient to both search and output sorted data through a binary tree. 
# I used it for part 2 because searching a binary tree is O(logn) in time complexity, versus a linked list which is an O(n). It is O(logn) because as it checks a certain node, it determines whether or not what youre searching for is less than or greater than, so it cuts the data in half. It repeats this until the data is either found or the tree is completely seached.
# I used it for part 4 because one of the main traversing methods for a binary tree is an in order traversal, which happens to output data in order from smallest to biggest. This makes it better because I am not using a secondary sorting algorithm on the data, which can take more time and memory. 

# STACK #
# I used a stack for part 3 because it helps to emulate the return and checking out process the best. When placing a pile of books to be returned, it only makes sense that you can take the top book off the stack and work from there. 
# A stack simulates this process the best because it is a data structure where last in first out, which is exactly how a pile of books for checking out and returning works.

# MIN HEAP #
# I used a minimum heap for part 5 because it was best suitable for storing the data based on priority. Once the data is put into the heap, its as simple as pulling out the root and re heapifying the heap to output the data in increasing order. 



# import files

from BST import BST
from BSTNode import BSTNode
from Stack import Stack
from Heap import Heap


# function to open txt file and store it
def books(txtFile):
    # declare binary tree
    books = BST()

    # open text file
    with open(txtFile, "r") as file:

        # iterate through text file, grabbing each line and storing the data in the binary tree
        for line in file:
            name, author, checked, priority = line.strip().split(", ")
            checked = int(checked)
            priority = int(priority)

            node = BSTNode(name=name, author=author, checked=checked, priority=priority)

            books.insert(node)

    return books


# function to find author
def findAuthor(tree, author):
    authorBooks = tree.findAuthorBooks(author)
    # the author exists and has books in catalog
    if authorBooks:
        for book in authorBooks:
            print("\n", book)
    # author doesn't exist
    else:
        print("\nAuthor Not Found")


# function to find a book
def findName(tree, name, flag=False):
    # find the book in the library
    book = tree.searchBook(name)
    # if the book is in the library and we are going to add it to a stack
    if flag and book:
        return book
    # if we just want to find the book
    if book:
        print("\n", book)
    else:
        print("\nBook Not Found")
        return -1
        

# function to check in or out books
def checkInOutBooks(tree, stack, returning):
    while not stack.isEmpty():
        bookNode = stack.pop()
        bookName = bookNode.name
        
        # make sure book is in the library
        foundBook = tree.searchBook(bookName)
        # returning books
        if foundBook and returning:
            if foundBook.checked == 1:
                print(f"\nBook {bookName} already checked in.")
            else:
                foundBook.checked = 1
                print(f"\nBook {bookName} returned successfully.")
        # checking out books
        elif foundBook and not returning:
            if foundBook.checked == 0:
                print(f"\nBook {bookName} already checked out") 
            else:
                foundBook.checked = 0
                print(f"\nBook {bookName} checked out successfully.")
        else:
            print(f"\nBook {bookName} not found in library catalog.")
            
# function to output books at the end of the day
def endOfDay(tree):
    # writes all the books to text file
    with open("EndOfDay.txt", "w") as file:
        # calls function to traverse tree, add book name and checked status to a list
        booksEndOfDay = tree.booksEndOfDay()
        for book, checked_status in booksEndOfDay:
            file.write(f"{book} is checked {"in" if checked_status == True else "out"}\n")
            
# funciton to add nodes to heap
def addBooksHeap(node):
    # base case
    if node is not None:
        # only adds nodes to heap if the book is checked in
        if node.checked == 1:
            booksHeap.push(node)
        # recursive calls
        addBooksHeap(node.left)
        addBooksHeap(node.right)
                        
# MAIN PROGRAM # 

# store all books in binary tree
booksFile = "SciFiLiBooks.txt"
booksTree = books(booksFile)

# Loop for user to keep interacting with code
while True:
        
    # Print a handy menu for user to use
    print("\nMenu:")
    print("1. List All Books")
    print("2. Search By Author")
    print("3. Search By Title")
    print("4. Return Books")
    print("5. Check Out Books")
    print("6. Close The Library")
    print("7. Library Catches Fire")
    
    # get the user choice
    userChoice = int(input("\nEnter your choice: "))
    
    # lists all of the books for user
    if userChoice == 1:
        booksTree.traverseInOrder()
        
    # lists all books by certain author        
    elif userChoice == 2:
        userAuthor = str(input("\nWhat author would you like to find? "))
        findAuthor(booksTree, userAuthor)
    
    # finds a book by name
    elif userChoice == 3:
        userName = str(input("\nWhat is the name of the book? "))
        findName(booksTree, userName)
    
    # returning books to the library
    elif userChoice == 4:
        # declare stack
        bookStack = Stack()
        # get a count of how many books are being returned
        returnCount = int(input("\nHow many books are you returning? "))
        while returnCount > 0:
            # get the names of the books to return
            returnBookName = str(input("\nWhat is the name of the book? "))
            # call function and set flag to True
            returnBook = findName(booksTree, returnBookName, True)
            # check if the book exists in library catalog, if not, returnCount not affected and user can redo name choice
            if returnBook != -1:
                # add book to stack
                bookStack.push(returnBook)
                # decrement return count
                returnCount -= 1
        # call return function to simulate book return, set the returning flag to True
        checkInOutBooks(booksTree, bookStack, True)
            
            
    elif userChoice == 5:
        # declare stack
        bookStack = Stack()
        # get a count of how many books are being checked out
        checkOutCount = int(input("\nHow many books are you checking out? "))
        while checkOutCount > 0:
            # get the names of books being checked out
            checkOutName = str(input("\nWhat is the name of the book? "))
            # call function and set flag to True
            checkOutBook = findName(booksTree, checkOutName, True)
            # check if the book exists in library catalog, if not, checkOutCount not affected and user can redo name choice
            if checkOutBook != -1:
                # add book to stack
                bookStack.push(checkOutBook)
                # decrement checkout count
                checkOutCount -= 1
        # call check out function to simulate checking out books, set the returning flag to False
        checkInOutBooks(booksTree, bookStack, False)
                
    # closing for the day
    elif userChoice == 6:
        # call function to write out library books to text file
        endOfDay(booksTree)
        print("\nGoodbye, see you tomorrow!")
        # exit loop
        break
    
    elif userChoice == 7:
        # declare heap
        booksHeap = Heap()
        # call function to traverse tree and add nodes to heap if they are in the library
        addBooksHeap(booksTree.root)
        print("\nBooks saved from fire (most important -> least imporant): \n")
        while not booksHeap.isEmpty():
            # get the maximum priority from the heap and print it out
            lostBook = booksHeap.pop()
            print(f"Book: {lostBook.name}, Priority: {lostBook.priority}")

        # library is burnt down, so exit loop
        print("\nGoing to have to start a new library!")
        break
