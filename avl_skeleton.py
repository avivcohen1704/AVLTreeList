#username - Eladk3
#id1      - 318730116
#name1    - Elad Kadosh
#id2      - 208637033
#name2    - Aviv Cohen


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
		self.height = -1
		self.size = 0


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
		return self.getValue()

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
		self.root = AVLNode() ## represents the virtual node for this specific tree
		self.min = None       ## both min & max are fields for first & last
		self.max = None


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
		if 0 > i or i > self.length():   ##list index out of range
			return None

		node = self.getRoot()

		cnt = 0
		while i > 1:                                        ## complexity O(logn) the height of the tree
			cnt += 1
			if cnt == node.getSize + 10:
				return "retrieve while-loop didnt stopped"   ##Retrieve check 1

			elif i < node.getLeft.getSize:
				node = node.getLeft
			elif i > node.getLeft.getSize:
				i = i - 1 - node.getLeft.getSize
				node = node.getRight
			elif i == node.getLeft.getSize:
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

		if i >= self.length() or i < 0:     ## list index out of range
			return 0

		newNode = AVLNode(val)  ## creates the new node that is going to be inserted

		if self.empty():        ## insert the first node to the tree
			virtualNode = self.root
			self.root = newNode
			self.min = newNode
			self.max = newNode

			newNode.setParent(virtualNode)
			newNode.setLeft(virtualNode)
			newNode.setRight(virtualNode)
			newNode.setHeight(0)
			newNode.size = 1

			return 0

		if i == self.length() or i == 1:    ## coplexcity O(1)
			if i == self.length():			## places newNode at the end of the list
				self.max.setRight(newNode)
				newNode.setParent(self.max)
				self.max = newNode

			elif i == 1:
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


		rotateCnt = 0
		"""here the tree will be the check if the tree needs to rotate, and if, will rotate (DNF coding rotating)
		
		afterwards we will compute all of the  fields"""


		return rotateCnt


	"""deletes the i'th item in the list

	@type i: int
	@pre: 0 <= i < self.length()
	@param i: The intended index in the list to be deleted
	@rtype: int
	@returns: the number of rebalancing operation due to AVL rebalancing
	"""
	def delete(self, i): ## DNF & first is basic
		if i > self.length():
			return

		return -1


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
		return self.root.getSize()

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
			return None
		n = node.getRight
		if node.getRight != None:
			while n.getLeft != None: ##Compexity O(logn)
				n = n.getLeft
			return n
		else:
			n = node
			while n.getParent.getLeft != n: ##Compexity O(logn)
				n = n.getParent
			return n

	def Predecessor(self, node):
		if node == self.min:
			return None
		n = node.getLeft
		if node.getLeft != None:
			while n.getRight != None:  ##Compexity O(logn)
				n=n.getRight
			return n
		else:
			n = node
			while n.getParent.getRight != n:  ##Compexity O(logn)
				n = n.getParent
			return n



