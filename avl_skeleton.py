#username - Eladk3
#id1      - 318730116
#name1    - Elad Kadosh
#id2      - 208637033
#name2    - Aviv Cohen

## update time == 31/3 10:30

"""A class represnting a node in an AVL tree"""

class AVLNode(object):
	"""Constructor, you are allowed to add more fields.

	@type value: str
	@param value: data of your node
	"""
	def __init__(self, value):
		self.value = value
		self.left = None
		self.right = None
		self.parent = None
		self.height = 0
		self.size = 1

	def virtualInit(self):    ## init of the node to be inserted into the tree
		self.left = self
		self.right = self
		self.parent = self
		self.size = 0
		self.setHeight(-1)

	"""returns the left child
	@rtype: AVLNode
	@returns: the left child of self, None if there is no left child
	"""
	def getLeft(self):
		return self.left

	"""returns the right child

	@rtype: AVLNode
	@returns: the right child of self, None if there is no right child
	"""
	def getRight(self):
		return self.right

	"""returns the parent 

	@rtype: AVLNode
	@returns: the parent of self, None if there is no parent
	"""
	def getParent(self):
		return self.parent

	"""return the value

	@rtype: str
	@returns: the value of self, None if the node is virtual
	"""
	def getValue(self):
		return self.value

	"""returns the height

	@rtype: int
	@returns: the height of self, -1 if the node is virtual
	"""
	def getHeight(self):
		return self.height

	"""sets left child

	@type node: AVLNode
	@param node: a node
	"""
	def setLeft(self, node):
		self.left = node
		return None

	"""sets right child

	@type node: AVLNode
	@param node: a node
	"""
	def setRight(self, node):
		self.right = node
		return None

	"""sets parent

	@type node: AVLNode
	@param node: a node
	"""
	def setParent(self, node):
		self.parent = node
		return None

	"""sets value

	@type value: str
	@param value: data
	"""
	def setValue(self, value):
		self.value = value
		return None

	"""sets the balance factor of the node

	@type h: int
	@param h: the height
	"""
	def setHeight(self, h):
		self.height = h
		return None

	"""returns whether self is not a virtual node 

	@rtype: bool
	@returns: False if self is a virtual node, True otherwise.
	"""
	def isRealNode(self):
		if self.height == -1:
			return False
		return True

	"""return the size of the node
	
	@rtype: int
	@returns: the size of the node, None if virtual
	"""
	def getSize(self):
		if self.isRealNode():
			return self.size
		else:
			return 0


"""
A class implementing the ADT list, using an AVL tree.
"""

class AVLTreeList(object):

	"""
	Constructor, you are allowed to add more fields.  

	"""
	def __init__(self):
		virtualNode = AVLNode("") 		  ## represents the virtual node for this specific tree
		virtualNode.virtualInit()         ## sets the virtual node to height -1 & size 0
		self.virtualNode = virtualNode    ## a field that represets a virtual node & can be used from all classes
		self.root = virtualNode           ## from here to ** set all roots pointers to VNode
		self.root.setLeft(virtualNode)
		self.root.setRight(virtualNode)
		self.root.setParent(virtualNode)  ## **
		self.min = self.root     		  ##  both min & max points at the root
		self.max = self.root


	"""returns whether the list is empty

	@rtype: bool
	@returns: True if the list is empty, False otherwise
	"""
	def empty(self): ##Supposed to be Done
		if self.root.getHeight == -1:
			return True
		return False

	"""retrieves the value of the i'th item in the list

	@type i: int
	@pre: 0 <= i < self.length()
	@param i: index in the list
	@rtype: str
	@returns: the the value of the i'th item in the list
	"""
	def retrieve(self, i):  ##Supposed to be finished

		node = self.getRoot()
		if node == None:
			return None
		len = self.length()
		cnt = 0

		while i >= 0:                                        ## complexity O(logn) the height of the tree

			cnt += 1
			if cnt == len + 10:
				return "retrieve while-loop didnt stopped"   ##Retrieve check 1
			elif i < node.getLeft().getSize():
				node = node.getLeft()
			elif i > node.getLeft().getSize():
				i = i - 1 - node.getLeft().getSize()
				node = node.getRight()
			elif i == node.getLeft().getSize():
				return node

		return "retrieve didnt work!!"                       ##Retrieve check 2

	"""inserts val at position i in the list

	@type i: int
	@pre: 0 <= i <= self.length()
	@param i: The intended index in the list to which we insert val
	@type val: str
	@param val: the value we inserts
	@rtype: list
	@returns: the number of rebalancing operation due to AVL rebalancing
	"""
	def insert(self, i, val): ## DNF, the insertion is ready, the rotating isn't, and the fields are not ready

		newNode = AVLNode(val)  ## creates the new node that is going to be inserted & init the new node stats
		newNode.setParent(self.virtualNode)
		newNode.setLeft(self.virtualNode)
		newNode.setRight(self.virtualNode)
		newNode.size = 1
		newNode.setHeight(0)

		if self.getRoot() == None:        ## insert the first node to the tree
			self.root = newNode
			self.min = newNode
			self.max = newNode

			return 0

		if i == self.length() or i ==0:   ## coplexcity O(1)
			if i == self.length():			## places newNode at the end of the list
				self.max.setRight(newNode)
				newNode.setParent(self.max)
				self.max = newNode

			elif i == 0:
				self.min.setLeft(newNode)   ## places newNode at the start of the list
				newNode.setParent(self.min)
				self.min = newNode

		else:
			oldNode = self.retrieve(i)  ## retrieves the i'th node - that is going to be replace, retrieve comlexity == O(logn)

			if oldNode.getLeft().getHeight == -1:
				oldNode.setLeft(newNode)
				newNode.setParent(oldNode)

			else:
				oldNodePre = self.Predecessor(oldNode)  ## finds the Predecessor of oldNode, complexity O(logn)
				oldNodePre.setRight(newNode)
				newNode.setParent(oldNodePre)

		rebalancingCNT = self.rebalancing(newNode)

		"""here the tree will be the check if the tree needs to rotate, and if, will rotate and return the number of balance actions (DNF coding rotating)"""
		is_need_rotation = self.is_Rotation(newNode.getParent())

		return is_need_rotation + rebalancingCNT

	"""deletes the i'th item in the list

	@type i: int
	@pre: 0 <= i < self.length()
	@param i: The intended index in the list to be deleted
	@rtype: int
	@returns: the number of rebalancing operation due to AVL rebalancing
	"""
	def delete(self, i): 							## deletion finished WO rotations
		if i == 0 and self.root.getHeight() == -1:
			return -1

		node = self.retrieve(i)
		mntcNode = node.getParent()					## maintance node, will be used to maintance fields
		if node.getHeight() == 0:  				    ## if node has no children, we erase him
			if node == self.getRoot():
				self.root = self.virtualNode
				return -1
			elif node.getParent().getRight() == node:
				node.getParent().setRight(self.virtualNode)
			else:
				node.getParent().setLeft(self.virtualNode)



		elif node.getRight().getHeight() != -1:		## node has right son, we replace the node with his suc
			sucNode = self.Succesor(node)
			if node.getRight() == sucNode:          ## suc is right son of node

				sucNode.setParent(node.getParent())          ## pointer changes
				node.getParent().setRight(sucNode)

				sucNode.setLeft(node.getLeft())
				node.getLeft().setParent(sucNode)

				mntcNode = sucNode

			else:                                   ## suc is not right son of node
				sucNode.getParent().setLeft(sucNode.getRight())        ## pointer chages

				sucNode.setParent(node.getParent())
				node.getParent().setRight(sucNode)

				sucNode.setLeft(node.getLeft())
				node.getLeft().setParent(sucNode)

				sucNode.setRight(node.getRight())
				node.getRight().setParent(sucNode)

				mntcNode = sucNode.getParent()


		else:
			preNode = self.Predecessor(node)		## node has left son, we replace the vals of him and his Pred
			if node.getLeft() == preNode:      		## pred is left son of node
				preNode.setParent(node.getParent())  ## pointer changes
				node.getParent().setLeft(preNode)

				preNode.setRight(node.getRight())
				node.getRight().setParent(preNode)

				mntcNode = preNode

			else:									## pred is not son if the node
				preNode.getParent().setRight(preNodeNode.getLeft())  ## pointer chages

				preNode.setParent(node.getParent())
				node.getParent().setLeftt(preNode)

				preNode.setRight(node.getRight())
				node.getRight().setParent(preNode)

				preNode.setLeft(node.getLeft())
				node.getLeft().setParent(preNode)

				mntcNode = preNode.getParent()

		node.virtualInit()  ##final deletion of the node
		self.virtualNode.virtualInit()  ##resets the tree's virtual node in case it had pointers somewhere

		rebalanceCNT = self.rebalancing(mntcNode)


		"""here we will have the rotations
		
		afterwards we will compute our fields"""

		return rebalanceCNT

	"""returns the value of the first item in the list

	@rtype: str
	@returns: the value of the first item, None if the list is empty
	"""
	def first(self):
		return self.min

	"""returns the value of the last item in the list

	@rtype: str
	@returns: the value of the last item, None if the list is empty
	"""
	def last(self):
		return self.max

	"""returns an array representing list 

	@rtype: list
	@returns: a list of strings representing the data structure
	"""
	def listToArray(self):  ##Supposed to be finished
		Array = []
		node = self.min
		i = 1
		while i <= self.length():
			Array.append(node.getValue)
			node = node.Succesor
			i +=1

		return Array

	"""returns the size of the list 

	@rtype: int
	@returns: the size of the list
	"""
	def length(self):  ## supposed to be finished
		return self.getRoot().getSize()

	"""splits the list at the i'th index

	@type i: int
	@pre: 0 <= i < self.length()
	@param i: The intended index in the list according to whom we split
	@rtype: list
	@returns: a list [left, val, right], where left is an AVLTreeList representing the list until index i-1,
	right is an AVLTreeList representing the list from index i+1, and val is the value at the i'th index.
	"""
	def split(self, i):
		return None

	"""concatenates lst to self

	@type lst: AVLTreeList
	@param lst: a list to be concatenated after self
	@rtype: int
	@returns: the absolute value of the difference between the height of the AVL trees joined
	"""
	def concat(self, lst):
		diff = abs(self.root.getHeight() - self.root.getHeight())  # what would be returned

		if self.getHeight() >= lst.getHeight():  # if self height >= lst height
			newRoot = self.Last()  # sets the last node of self to be the new root
			newRoot.setRight(lst.root)  # sets the roots of self & lst to be the L & R sos of the new root
			newRoot.setLeft(self.root)
			self.delete(self.getSize())  # deletes newRoot from self

			while abs(self.balancefactor(
					newRoot)) > 1:  # "glides" alone self until the height matches self's height complexity O(logm) m = size of self
				if newRoot.balancefactor() > 0:
					newRoot.setLeft(newRoot.getLeft().getRight())
					if abs(self.balancefactor(newRoot)) < 1:
						newRoot.setParent(newRoot.getLeft().getParent())
						newRoot.getParent().setLeft(newRoot)
				else:
					newRoot.setRight(newRoot.getRight().getLeft())
					if abs(self.balancefactor(newRoot)) > 1:
						newRoot.setParent(newRoot.getRight().getParent())
						newRoot.getParent().setLeft(newRoot)

			rotationNode = newRoot

			while rotationNode.getParent().getHeight() != -1:  # makes the rotations up self tree O(logm) m = size of self
				rotationNode.checkForRotationNeed()
				rotationNode = rotationNode.getParent()

		else:  # if self height < lst height
			newRoot = lst.First()
			newRoot.setRight(lst.root)
			newRoot.setLeft(self.root)
			lst.delete(0)

			while abs(self.balancefactor(
					newRoot)) > 1:  # "glides" alone self until the height matches self's height complexity O(logm) m = size of self
				if newRoot.balancefactor() > 0:
					newRoot.setLeft(newRoot.getLeft().getRight())
					if abs(self.balancefactor(newRoot)) < 1:
						newRoot.setParent(newRoot.getLeft().getParent())
						newRoot.getParent().setLeft(newRoot)
				else:
					newRoot.setRight(newRoot.getRight().getLeft())
					if abs(self.balancefactor(newRoot)) > 1:
						newRoot.setParent(newRoot.getRight().getParent())
						newRoot.getParent().setLeft(newRoot)

			rotationNode = newRoot

			while rotationNode.getParent().getHeight() != -1:
				rotationNode.checkForRotationNeed()
				rotationNode = rotationNode.getParent()

		return diff

	"""searches for a *value* in the list

	@type val: str
	@param val: a value to be searched
	@rtype: int
	@returns: the first index that contains val, -1 if not found.
	"""
	def search(self, val):  ## supposed to be Done
		node = self.min
		while node.getValue != val:
			node = node.Succesor
		return node

	"""returns the root of the tree representing the list

	@rtype: AVLNode
	@returns: the root, None if the list is empty
	"""
	def getRoot(self):
		if self.root.height == -1:
			return None
		return self.root

	"""returns the succesor of a given node
	
	@rtype: AVLNode
	@returns: the succesor of the node, virtual node if has no succesor
	"""
	def Succesor(self, node):
		if node == self.max:
			return node.getRight()
		n = node.getRight()
		if node.getRight().getHeight() != -1:
			while n.getLeft().getHeight() != -1: ##Compexity O(logn)
				n = n.getLeft()
			return n
		else:
			n = node
			while n.getParent().getLeft() != n: ##Compexity O(logn)
				n = n.getParent()
			return n

	"""returns the predecessor of a given node

	@rtype: AVLNode
	@returns: the predecessor of the node, virtual node if has no predecessor
	"""
	def Predecessor(self, node):
		if node == self.min:
			return node.getLeft()
		n = node.getLeft()
		if node.getLeft().getHeight() != -1:
			while n.getRight().getHeight() != -1:  ##Compexity O(logn)
				n=n.getRight()
			return n
		else:
			n = node
			while n.getParent().getRight() != n:  ##Compexity O(logn)
				n = n.getParent()
			return n

	""" maintance the fields of the tree from a node up to the root, returns the sum of changes
	
	@rtype: AVLNode
	@returns: the number of height changes that were made
	"""
	def rebalancing(self, node):
		cnt = 0
		h = max(node.getLeft().getHeight(), node.getRight().getHeight()) + 1    #computes only for the node itself
		s = node.getLeft().getSize() + 1 + node.getRight().getSize()
		if h != node.getHeight():
			cnt += 1
		if s != node.getSize():
			cnt+=1
		node.setHeight(h)
		node.size = s

		while node.getParent().getHeight() != -1: ## computes for all ancestors, comlexity O(logn)
			node = node.getParent()
			h = max(node.getLeft().getHeight(), node.getRight().getHeight()) + 1   		# h is height value
			s = node.getLeft().getSize() + 1 + node.getRight().getSize()				# s is size value
			if h != node.getHeight():
				cnt += 1
			if s != node.getSize():
				cnt += 1
			node.setHeight(h)
			node.size = s

		return cnt

	""" computes the balance factor of a given node
	
	@rtype: AVLNode
	@returns the node's balance factor
	"""
	def balancefactor(self, node):
		return node.getLeft().getHeight() - node.getRight().getHeight()

	""" left rotation (BF = -2 and BF OF RIGHT SON = -1)

        C                              B
            \       Left Rotation        / \
            B    - - - - - - - >       C   A 
           \                           
            A

    """
	def left_rotation(self, C):
		direction = "root"
		if C.getParent() != self.virtualNode:  ## if C is not root
			if C.getParent().getLeft() == C:
				direction = 'L'
			else:
				direction = 'R'

		## change the indexes of B, C (NOT A)
		B = C.getRight()
		C.setRight(B.getLeft())
		C.getRight().setParent(C)  ### den VNodeinit?
		B.setLeft(C)
		B.setParent(C.getParent())
		C.setParent(B)

		## connect C parent to B from left or right
		if direction == 'L':
			C.getParent().setLeft(B)
		elif direction == 'R':
			C.getParent().setRight(B)
		else:
			self.root = B
		self.virtualNode.virtualInit()
		cnt = self.rebalancing(C)
		return cnt

	""" right rotation (BF = +2 and BF OF LEFT SON = +1)

           C                               B
             /       Right Rotation          / \
         B        - - - - - - - >        A   C 
        /                                
       A

    """
	def right_rotation(self, C):
		direction = "root"
		if C.getParent() != self.virtualNode:  ## if C is not root
			if C.getParent().getLeft() == C:
				direction = 'L'
			else:
				direction = 'R'

		## change the indexes of B, C (NOT A)
		B = C.getLeft()
		C.setLeft(B.getRight())
		C.getLeft().setParent(C)
		B.setRight(C)
		B.setParent(C.getParent())
		C.setParent(B)

		## connect C parent to B from left or right
		if direction == 'L':
			C.getParent().setLeft(B)
		elif direction == 'R':
			C.getParent().setRight(B)
		else:
			self.root = B
		self.virtualNode.virtualInit()
		cnt = self.rebalancing(C)
		return cnt

	""" left then right rotation (BF = +2 and BF OF LEFT SON = -1)

           C                               C                         B
             /    Left Right Rotation        /                         / \
         A       - - - - - - - >         B       - - - - - - - >   A   C
          \                             /                                   
           B                           A                                 

    """
	def left_right_rotation(self, C):
		cnt = self.left_rotation(C.getLeft())  ## rotation left of A,B
		cnt += self.right_rotation(C)  ## rotation right of B, C
		return cnt

	""" right then left rotation (BF = -2 and BF OF RIGHT SON = +1)

           A                               A                             B
               \    Right Left Rotation        \                           / \
             C     - - - - - - - >           B       - - - - - - - >   A   C
            /                                 \                                   
           B                                   C                          

    """
	def right_left_rotation(self, A):
		cnt = self.right_rotation(A.getRight())  ## rotation right of B, C
		cnt += self.left_rotation(A)  ## rotation left of A, B
		return cnt

	""" the function check if the tree need rotations, from the specific node to the root, and return the number of balancing actions
    """
	def is_Rotation(self, node):

		rebalancingCNT = 0
		while node.getHeight() != -1:

			bf = self.balancefactor(node)  ## check the balance factor of the node

			## if the bf is OK continue to the parent until u reach to the root
			if (abs(bf) < 2):
				node = node.getParent()

			## the bf is not OK, so do one of the rotations
			else:
				if (bf == -2):
					if ((self.balancefactor(node.getRight())) == -1):
						## bf of right son is -1
						rebalancingCNT = self.left_rotation(node)
					else:
						## bf of right son is +1
						rebalancingCNT = self.right_left_rotation(node)
				elif (bf == 2):
					if (AVLTreeList.balancefactor(node.getRight()) == 1):
						## bf of left son is +1
						rebalancingCNT = self.right_rotation(node)
					else:
						## bf of left son is -1
						rebalancingCNT = self.left_right_rotation(node)
				break  ## do only one rotation

		return rebalancingCNT

	""" the function print the first n elements in the tree
	"""
	def print_Tree(self, n):
		for i in range(n):
			t = tree.retrieve(i)
			print("")
			print("        Parent " + t.getParent().getValue())
			print("           |")
			print("         Node " + t.getValue())
			print("      /         \\")
			print("left son " + t.getLeft().getValue() + "     right son " + t.getRight().getValue())
			print("")
		return








"""
############
###TESTER###
############
"""




tree = AVLTreeList()

print("###############")

tree.insert(0, "C")
tree.print_Tree(1)

print("###############")


tree.insert(1, "B")
tree.print_Tree(2)

print("###############")


tree.insert(2, "A")
tree.print_Tree(3)

print("###############")

tree.insert(3, "Z")
tree.print_Tree(4)

print("###############")

tree.insert(4, "P")
tree.print_Tree(4)
print(tree.retrieve(0).getValue())
print(tree.retrieve(1).getValue())
print(tree.retrieve(2).getValue())
print(tree.retrieve(3).getValue())
print(tree.retrieve(4).getValue())