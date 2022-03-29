#username - Eladk3
#id1      - 318730116
#name1    - Elad Kadosh
#id2      - 208637033
#name2    - Aviv Cohen

## update time == 27/3 2130

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
		virtualNode = AVLNode("") ## represents the virtual node for this specific tree
		virtualNode.virtualInit()         ## sets the virtual node to height -1 & size 0
		self.virtualNode = virtualNode    ## a field that represets a virtual node & can be used from all classes
		self.root = virtualNode           ## from here to ** set all roots pointers to VNode
		self.root.setLeft(virtualNode)
		self.root.setRight(virtualNode)
		self.root.setParent(virtualNode)   ## **
		self.min = self.root     ##  both min & max points at the root
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


	def balancefactor(self, node):
		return node.getLeft.gethight() - node.getRight.gethight()

	def left_rotation(self, B):

		return

	def right_rotation(self, B):
		A = B.getLeft()
		B.setLeft(A.getRight())
		B.getLeft().setParent(B)
		A.setRight(B)
		A.setParent(B.getParent())
		if (B.getParent().getLeft() == B):
			A.getParent().setLeft(A)
		else:
			A.getParent().setRight(A)
		B.setParent(A)
		return

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


		"""here the tree will be the check if the tree needs to rotate, and if, will rotate (DNF coding rotating)"""


		node_rotation = newNode.getParent()

		"""
		while node_rotation.getHeight() != -1:
			bf = AVLTreeList.balancefactor(node_rotation)

			if (abs(bf) < 2):
				node_rotation = node_rotation.getParent()
			else:
				rotateCnt += 1
				if (bf == -2):
					if (AVLTreeList.balancefactor(node_rotation.getRight) == -1):
						AVLTreeList.left_rotation(node_rotation)
					else:
						AVLTreeList.right_rotation(node_rotation)
						AVLTreeList.left_rotation(node_rotation)
				elif (bf == 2):
					if (AVLTreeList.balancefactor(node_rotation.getRight) == 1):
						AVLTreeList.right_rotation(node_rotation)
					else:
						AVLTreeList.left_rotation(node_rotation)
						AVLTreeList.right_rotation(node_rotation)
				break 	## in insertion we have at most 1 rotation
`		"""


		return rebalancingCNT


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
		if node.getHeight() == 0:    ## if node has no children, we erase him
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
		return None

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


	""" maintance the fields of the tree from a node up
	returns the sum of changes
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


"""TESTER"""
tree = AVLTreeList()
tree.insert(0,"a")
tree.insert(0, "b")
tree.insert(0, "c")

print(tree.retrieve(0).getHeight(), tree.retrieve(1).getHeight(), tree.retrieve(2).getHeight())

tree.delete(0)
print(tree.retrieve(0).getHeight(), tree.retrieve(1).getHeight())

tree.retrieve(1)
tree.delete(0)
tree.delete(0)

print(tree.retrieve(0))

"""
for i in range(3):
	t = tree.retrieve(i)
	print("node " + t.getValue())
	print("parent " + t.getParent().getValue())
	print("left son " + t.getLeft().getValue())
	print("right son " + t.getRight().getValue())

tree.right_rotation(tree.retrieve(2))
print()

for i in range(3):
	t = tree.retrieve(i)
	print("node " + t.getValue())
	print("parent " + t.getParent().getValue())
	print("left son " + t.getLeft().getValue())
	print("right son " + t.getRight().getValue())
"""