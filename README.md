# Python AVL-Based List ADT

### This project implements a List ADT using an AVL tree. The implementation is based on Python 3.9, adhering to the skeleton code provided on the course website.

## Features
1. empty(): Checks if the list is empty.
2. retrieve(i): Retrieves the value of the element at index i or returns None if it doesn't exist.
3. insert(s, i): Inserts an element with value s at index i. Returns the total number of rebalancing operations performed during tree correction.
4. delete(i): Deletes the element at index i if it exists. Returns the total number of rebalancing operations or -1 if insufficient items exist.
5. first(): Returns the value of the first item or None if the list is empty.
6. last(): Returns the value of the last item or None if the list is empty.
7. listToArray(): Returns an array containing the list elements in order of their indices or an empty array if the list is empty.
8. length(): Returns the number of items in the list.
9. split(i): Splits the list at index i.
10. concat(lst): Appends the list lst to the current list.
11. search(val): Returns the index of the first occurrence of val in the list or -1 if not found.

## AVLNode Class
The AVLNode class serves as the building block of the AVL tree. Every leaf node has two "virtual" children, making rotations easier without special edge case handling. The AVLNode class has the following methods:

 - **getHeight()**: Returns the height of the node or -1 if the node is virtual.
- **getValue()**: Returns the info value of the node or None if the node is virtual.
- **getLeft()**: Returns the left child or None.
- **getRight()**: Returns the right child or None.
- **getParent()**: Returns the parent node or None.
- **isRealNode()**: Checks if the node is real (i.e., not virtual).

## Important Notes
1. This implementation is based on filling in the provided skeleton code. Additional helper functions may be added, but the existing function specifications should not be altered.
2. The project does not utilize any library-based data structure implementations.

## Complexity Documentation
Each function's worst-case time complexity is documented both in the code and in a separate detailed document. Every effort has been made to achieve the lowest possible time complexity for each function.

## Output
No user output is required.


## Running the AVL-Based List ADT
### 1. Prerequisites
Ensure you have Python installed. If not, download and install it from the official Python website.

### 2. Clone the Repository
```
git clone [YOUR_REPOSITORY_URL]
cd [YOUR_REPOSITORY_DIRECTORY]
```
### 3. Running the Code
If you want to see the AVL-Based List ADT in action, you can run the provided sample program:
```
python avl_list.py
```
This will execute the file and any sample operations or tests included in avl_list.py.

## Using the AVL-Based List ADT in Your Own Projects
You can import the AVL list and use its functions as follows:
```
from avl_list import AVLList

# Create a new AVL list
my_list = AVLList()

# Add some elements
my_list.insert(10)
my_list.insert(20)

# Print the list
print(my_list)

# ... and so on for other operations!
```
