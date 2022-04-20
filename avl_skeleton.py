#username - Eladk3
#id1      - 318730116
#name1    - Elad Kadosh
#id2      - 208637033
#name2    - Aviv Cohen

## update time == 20/04 1500

"""A class represnting a node in an AVL tree"""

class AVLNode(object):
	"""
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

	"""resets the fields of a virtual node, O(1)
	
	"""
	def virtualInit(self):
		self.left = self
		self.right = self
		self.parent = self
		self.size = 0
		self.setHeight(-1)

	"""returns the left child, O(1)
	@rtype: AVLNode
	@returns: the left child of self, None if there is no left child
	"""
	def getLeft(self):
		return self.left

	"""returns the right child, O(1)

	@rtype: AVLNode
	@returns: the right child of self, None if there is no right child
	"""
	def getRight(self):
		return self.right

	"""returns the parent, O(1)

	@rtype: AVLNode
	@returns: the parent of self, None if there is no parent
	"""
	def getParent(self):
		return self.parent

	"""return the value, O(1)

	@rtype: str
	@returns: the value of self, None if the node is virtual
	"""
	def getValue(self):
		return self.value

	"""returns the height, O(1)

	@rtype: int
	@returns: the height of self, -1 if the node is virtual
	"""
	def getHeight(self):
		return self.height

	"""sets left child, O(1)

	@type node: AVLNode
	@param node: a node
	"""
	def setLeft(self, node):
		self.left = node
		return None

	"""sets right child, O(1)

	@type node: AVLNode
	@param node: a node
	"""
	def setRight(self, node):
		self.right = node
		return None

	"""sets parent, O(1)

	@type node: AVLNode
	@param node: a node
	"""
	def setParent(self, node):
		self.parent = node
		return None

	"""sets value, O(1)

	@type value: str
	@param value: data
	"""
	def setValue(self, value):
		self.value = value
		return None

	"""sets the height of the node, O(1)

	@type h: int
	@param h: the height
	"""
	def setHeight(self, h):
		self.height = h
		return None

	"""returns whether self is not a virtual node, O(1)

	@rtype: bool
	@returns: False if self is a virtual node, True otherwise.
	"""
	def isRealNode(self):
		if self.height == -1:
			return False
		return True

	"""return the size of the node, O(1)
	
	@rtype: int
	@returns: the size of the node
	"""
	def getSize(self):
		return self.size


"""
A class implementing the ADT list, using an AVL tree.
"""

class AVLTreeList(object):

	"""
	 initialize a new AVL Tree List,O(1)
	"""
	def __init__(self):
		virtualNode = AVLNode(None) 		  ## represents the virtual node for this specific tree
		virtualNode.virtualInit()         ## sets the virtual node to height -1 & size 0
		self.virtualNode = virtualNode    ## a field that represets a virtual node & can be used from all classes
		self.root = virtualNode           ## from here to ** set all roots pointers to VNode
		self.root.setLeft(virtualNode)
		self.root.setRight(virtualNode)
		self.root.setParent(virtualNode)  ## **
		self.min = self.root     		  ##  both min & max points at the root
		self.max = self.root


	"""returns whether the list is empty, O(1)

	@rtype: bool
	@returns: True if the list is empty, False otherwise
	"""
	def empty(self):
		if self.root.getHeight() == -1:
			return True
		return False

	"""retrieves the value of the i'th item in the list using retrieveNode, O(logn)

	@type i: int
	@pre: 0 <= i < self.length()
	@param i: index in the list
	@rtype: str
	@returns: the the value of the i'th item in the list
	"""
	def retrieve(self,i):
		if self.retrieveNode(i) == None:
			return None
		return self.retrieveNode(i).getValue()   			# uses retrieveNode to get the value of the i'th item \n
															# O(logn)

	"""retrieves the i'th node in the tree O(logn)
	"""
	def retrieveNode(self, i):

		node = self.getRoot()						# node - the pointer we are going to chage
		if node == None:
			return None

		len = self.length()
		cnt = 0

		while i >= 0:                                        	# complexity O(logn) the height of the tree

			if i < node.getLeft().getSize():					# The node is in the left subtree
				node = node.getLeft()
			elif i > node.getLeft().getSize():					# The node is in the right subtree
				i = i - 1 - node.getLeft().getSize()
				node = node.getRight()
			elif i == node.getLeft().getSize():					# we have found the node
				return node


	"""inserts val at position i in the list, O(logn)

	@type i: int
	@pre: 0 <= i <= self.length()
	@param i: The intended index in the list to which we insert val
	@type val: str
	@param val: the value we inserts
	@rtype: list
	@returns: the number of rebalancing operation due to AVL rebalancing
	"""
	def insert(self, i, val):
		cnt = 0   										# counter for rebalancing
		newNode = AVLNode(val) 							# creates the new node that is going to be inserted & \n
														# init the new node stats
		newNode.setParent(self.virtualNode)
		newNode.setLeft(self.virtualNode)
		newNode.setRight(self.virtualNode)
		newNode.size = 1
		newNode.setHeight(0)

		if self.getRoot() == None:       				# if the list is empyu inserts the first node to the tree
			self.root = newNode
			self.min = newNode
			self.max = newNode

			return 0

		if i == self.length() or i ==0:   				# if the node is going to be inserted in first or last
			if i == self.length():						# places newNode at the end of the list
				self.max.setRight(newNode)
				newNode.setParent(self.max)
				self.max = newNode

			elif i == 0:
				self.min.setLeft(newNode)   			# places newNode at the start of the list
				newNode.setParent(self.min)
				self.min = newNode

		else:											# is not 0 or as the length of the list or the root
			oldNode = self.retrieveNode(i)  				# retrieves the i'th node - that is going to be replace,\n
														# retrieve comlexity == O(logn)

			if oldNode.getLeft().getHeight() == -1: 		#if oldNode.left is a leaf, we insert to his left
				oldNode.setLeft(newNode)
				newNode.setParent(oldNode)

			else:											# oldNode is not a leaf, we inset to his predecessors right
				oldNodePre = self.Predecessor(oldNode)      # finds the Predecessor of oldNode, complexity O(logn)
				oldNodePre.setRight(newNode)
				newNode.setParent(oldNodePre)

		cnt += self.rebalancing(newNode)          			# keeps height & size feilds
		cnt += self.is_Rotation(newNode.getParent())     	# rotates the tree

		return cnt

	"""deletes the i'th item in the list, O(logn)

	@type i: int
	@pre: 0 <= i < self.length()
	@param i: The intended index in the list to be deleted
	@rtype: int
	@returns: the number of rebalancing operation due to AVL rebalancing
	"""
	def delete(self, i):
		if i >= self.length() or i < 0:
			return -1
		cnt = 0  												# counter for rebalancing

		if i == 0 and self.root.getHeight() == -1:  			# the tree is empty
			return -1

		if self.length() == 1:									# the tree have 1 node
			self.root = self.virtualNode
			self.max = self.virtualNode
			self.min = self.virtualNode
			return 0

		node = self.retrieveNode(i)                      			# finds the node we are going to delete, O(logn)
		root = False											# boolean that will be true iff the node is the root
		if self.root == node:
			root = True

		min = False												# booleans that will be true iff the node is first or last
		max = False
		if self.min == node or self.max == node:
			if self.min == node:
				min = True
			if self.max == node:
				max = True

		mntcNode = node.getParent()					            # marks the maintance node, will be used \n
																# to maintance fields
		if node.getHeight() == 0:  				    			# if node has no children, we delete him
			if root:
				self.root = self.virtualNode
				return 0										# we return 0 because no rebalancin is needed
			elif node.getParent().getRight() == node:			# node is a right child
				node.getParent().setRight(self.virtualNode)
			else:												# node is a left child
				node.getParent().setLeft(self.virtualNode)



		elif node.getRight().getHeight() != -1:					# node has right son, we replace the node with his suc
			sucNode = self.Succesor(node)
			if node.getRight() == sucNode:          			# suc is right son of node
				sucNode.setParent(node.getParent())          	# pointer change

				if node.getParent().getRight() == node:
					node.getParent().setRight(sucNode)
				else:
					node.getParent().setLeft(sucNode)

				sucNode.setLeft(node.getLeft())					# maintaning the pointers
				node.getLeft().setParent(sucNode)
				mntcNode = sucNode

			else:                                   				# suc is not right son of node
				sucNode.getRight().setParent(sucNode.getParent())
				mntcNode = sucNode.getParent()						# maintance node, will be used to maintance fields
				sucNode.getParent().setLeft(sucNode.getRight())     # pointers chage
				sucNode.setParent(node.getParent())

				if node.getParent().getRight() == node:				# node is a right child
					node.getParent().setRight(sucNode)
				else:
					node.getParent().setLeft(sucNode)				# node is a left child

				sucNode.setLeft(node.getLeft())						# maintaning the pointers
				node.getLeft().setParent(sucNode)
				sucNode.setRight(node.getRight())
				node.getRight().setParent(sucNode)

			if root:
				self.root = sucNode

		else:
			preNode = self.Predecessor(node)					# node doesnt have a left son, we replace the \n
																# him and his Predeccessor , complexity O(logn)
			if node.getLeft() == preNode:      					# pred is left son of node
				preNode.setParent(node.getParent())  			# pointer changes

				if node.getParent().getRight() == node:			#node is a right child
					node.getParent().setRight(preNode)
				else:											# node is a left child
					node.getParent().setLeft(preNode)

				preNode.setRight(node.getRight())				# maintaning the pointers
				node.getRight().setParent(preNode)
				mntcNode = preNode

			else:														# pred is not son if the node
				mntcNode = preNode.getParent()
				preNode.getParent().setRight(preNodeNode.getLeft())  	# pointers chage
				preNode.setParent(node.getParent())

				if node.getParent().getLeft() == node:					#node is a left child
					node.getParent().setLeft(preNode)
				else:													#node is a right child
					node.getParent().setRight(preNode)

				preNode.getLeft().setParent(preNode.getParent())		# maintaning the pointers
				preNode.setRight(node.getRight())
				node.getRight().setParent(preNode)
				preNode.setLeft(node.getLeft())
				node.getLeft().setParent(preNode)

			if root:
				self.root = preNode

		if min or max:											# if the node is deleted from last or first \n
																# update the fields
			MMNode = self.getRoot()								# Marks MinMaxNode
			if min:
				while MMNode.getLeft().getHeight() != -1:
					MMNode = MMNode.getLeft()
				self.min = MMNode
			else:
				while MMNode.getRight().getHeight() != -1:
					MMNode = MMNode.getRight()
				self.max = MMNode


		node.virtualInit()  									#final deletion of the node
		self.virtualNode.virtualInit()  						# resets the tree's virtual node in \n
																# case it had pointers somewhere

		cnt += self.rebalancing(mntcNode)

		cnt += self.is_Rotation(mntcNode)


		return cnt

	"""returns the value of the first item in the list, O(1)

	@rtype: str
	@returns: the value of the first item, None if the list is empty
	"""
	def first(self):
		return self.min.getValue()

	"""returns the value of the last item in the list, O(1)

	@rtype: str
	@returns: the value of the last item, None if the list is empty
	"""
	def last(self):
		return self.max.getValue()

	"""returns an array representing list, O(n)

	@rtype: list
	@returns: a list of strings representing the data structure
	"""
	def listToArray(self):
		Array = []									# the array we are going to return
		node = self.min
		i = 1
		while i <= self.length():                  	# O(n) - proved in calss
			Array.append(node.getValue())
			node = self.Succesor(node)
			i +=1

		return Array

	"""returns the size of the list, O(1)

	@rtype: int
	@returns: the size of the list
	"""
	def length(self):
		return self.root.getSize()

	"""splits the list at the i'th index, O(logn)
	@type i: int
	@pre: 0 <= i < self.length()
	@param i: The intended index in the list according to whom we split
	@rtype: list
	@returns: a list [left, val, right], where left is an AVLTreeList representing the list until index i-1,
	right is an AVLTreeList representing the list from index i+1, and val is the value at the i'th index.
	"""
	def split(self, i):

		splinter = self.retrieveNode(i)				# splinter is the intended node in the list according to whom we split
		rightTree = AVLTreeList()
		leftTree = AVLTreeList()
		if i == 0:
			self.delete(0)
			rightTree = self
			split_list = []
			split_list.append(leftTree)
			split_list.append(splinter.getValue())
			split_list.append(rightTree)
			return split_list

		# if splinter have left son build left tree
		if splinter.getLeft().getHeight() != -1:
			leftTree.root = splinter.getLeft()
			leftTree.min = leftTree.get_min()
			leftTree.max = leftTree.get_max()
			leftTree.root.setParent(self.virtualNode)		# separate the subtree from the original tree
		# if splinter have right son build right tree
		if splinter.getRight().getHeight() != -1:
			rightTree.root = splinter.getRight()
			rightTree.min = rightTree.get_min()
			rightTree.max = rightTree.get_max()
			rightTree.root.setParent(self.virtualNode)		# separate the subtree from the original tree
		splinter.setLeft(self.virtualNode)
		splinter.setRight(self.virtualNode)
		current = splinter
		while current.getParent().getHeight() != -1:
			parent = current.getParent()
			# current is the right son
			if parent.getRight() == current:
				connector = AVLNode(parent.getValue())		# the node we want to connect with
				connector.setParent(self.virtualNode)
				connector.setLeft(self.virtualNode)
				connector.setRight(self.virtualNode)
				subLeft = AVLTreeList()
				if parent.getLeft().getHeight() != -1:
					subLeft.root = parent.getLeft()
					subLeft.min = subLeft.get_min()
					subLeft.max = subLeft.get_max()
					subLeft.root.setParent(self.virtualNode)
					parent.setLeft(self.virtualNode)
				# joining subtree with left tree by connector
				leftTree = subLeft.join(connector, leftTree)
			# current is the left son
			else:
				connector = AVLNode(parent.getValue())		# the node we want to connect with
				connector.setParent(self.virtualNode)
				connector.setLeft(self.virtualNode)
				connector.setRight(self.virtualNode)
				subRight = AVLTreeList()
				if parent.getRight().getHeight() != -1:
					subRight.root = parent.getRight()
					subRight.min = subRight.get_min()
					subRight.max = subRight.get_max()
					subRight.root.setParent(self.virtualNode)
					parent.setRight(self.virtualNode)
				# joining subtree with right tree by connector
				rightTree = rightTree.join(connector, subRight)
			current = current.getParent()
		# updating min/max at the new trees
		leftTree.min = leftTree.get_min()
		leftTree.max = leftTree.get_max()
		rightTree.min = rightTree.get_min()
		rightTree.max = rightTree.get_max()
		# creating the return list and adding the trees to the list, with splinter
		split_list = []
		split_list.append(leftTree)
		split_list.append(splinter.getValue())
		split_list.append(rightTree)
		return split_list

	"""concatenates lst to self

	@type lst: AVLTreeList
	@param lst: a list to be concatenated after self
	@rtype: int
	@returns: the absolute value of the difference between the height of the AVL trees joined
	"""
	def concat(self, lst):

		if self.empty():									# self is empty
			self.virtualNode = lst.virtualNode
			self.root = lst.root
			self.min = lst.min
			self.max = lst.max
			return lst.root.getHeight() + 1
		elif lst.empty():									# lst is empty
			return self.root.getHeight() + 1

		diff = abs(self.root.getHeight() - lst.getRoot().getHeight())		#what will be returned

		height1IsBigger = True
		if self.root.getHeight() < lst.root.getHeight():				# marks which tree is higher
			height1IsBigger = False

		newRoot = self.max						# will be root after concat
		mntcNode = newRoot.getParent()

		if newRoot == self.root:
			if newRoot.getLeft().getHeight() == -1:			#self have only 1 node
				self.virtualNode = lst.virtualNode
				self.root = lst.root
				self.min = lst.min
				self.max = lst.max
				self.insert(0, newRoot.getValue())
				return lst.root.getHeight() -1
			self.root = newRoot.getLeft()
			mntcNode = self.root

		oldRoot = self.root
		if not height1IsBigger:								# the root of the higher tree
			oldRoot = lst.root

		newRoot.getLeft().setParent(newRoot.getParent())    # removes newRoot from original place*
		self.virtualNode.virtualInit()
		newRoot.getParent().setRight(newRoot.getLeft())
		self.virtualNode.virtualInit()						#*

		newRoot.virtualInit()								# resets newRoots fields
		newRoot.setHeight(0)


		self.rebalancing(mntcNode)						# maintance of the fields, O(logn)
		self.is_Rotation(mntcNode)							# rotates the tree, O(logn)

		newRoot.setLeft(self.root)							# insert NR into root*
		newRoot.setRight(lst.root)
		newRoot.setParent(self.virtualNode)
		self.root.setParent(newRoot)
		lst.root.setParent(newRoot)							#*


		self.rebalancing(mntcNode)						# maintance of the fields, O(logn)


		if height1IsBigger:
			glide = False					# marks if new root is not the root
			while self.balancefactor(newRoot) != 0 and self.balancefactor(newRoot) != 1:	#search for the first \n
																							#node that BF is 0 or 1 \n
																							#O(logn)
				glide = True
				newRoot.setLeft(newRoot.getLeft().getRight())

			if glide:													# if the root is changed
				oldRoot.setParent(self.virtualNode)

				newRoot.setParent(newRoot.getLeft().getParent())  		#connects NR to his new place down lst
				newRoot.getParent().setRight(newRoot)
				newRoot.getLeft().setParent(newRoot)


			self.rebalancing(newRoot)								# maintance of the fields, O(logn)
			self.is_Rotation(newRoot)								# rotates the tree, O(logn)

		elif not height1IsBigger:
			glide = False					# marks if new root is not the root
			while self.balancefactor(newRoot) != 0 and self.balancefactor(newRoot) != -1:	#search for the first \n
																							#node that BF is 0 or -1 \n
																							#O(logn)
				glide = True
				newRoot.setRight(newRoot.getRight().getLeft())

			if glide:													# if the root is changed
				oldRoot.setParent(self.virtualNode)

				newRoot.setParent(newRoot.getRight().getParent())		#connects NR to his new place down lst
				newRoot.getParent().setLeft(newRoot)
				newRoot.getRight().setParent(newRoot)

			self.rebalancing(newRoot)								# maintance of the fields, O(logn)
			self.is_Rotation(newRoot)								# rotates the tree, O(logn)

		finalRoot = newRoot
		while finalRoot.getParent().getHeight() != -1:			#search for the final root, O(logn)
			finalRoot = finalRoot.getParent()
		self.root = finalRoot

		self.max = lst.max
		return diff

	"""searches for a *value* in the list, O(i) i as the index of the value in the list

	@type val: str
	@param val: a value to be searched
	@rtype: int
	@returns: the first index that contains val, -1 if not found.
	"""
	def search(self, val):
		if self.root.getHeight() == -1:
			return -1
		cnt = 0
		node = self.min
		if node.getValue() == val:
			return 0
		if node == self.max:
			return -1
		while node.getValue() != val:			#O(i) i as the index of the value in the list - proved in class
			cnt += 1
			node = self.Succesor(node)

			if cnt > self.length():
				return -1
		return cnt

	"""returns the root of the tree representing the list, O(1)

	@rtype: AVLNode
	@returns: the root, None if the list is empty
	"""
	def getRoot(self):
		if self.root.height == -1:
			return None
		return self.root

	"""returns the succesor of a given node, WC - O(logn)
	
	@rtype: AVLNode
	@returns: the succesor of the node, virtual node if has no succesor
	"""
	def Succesor(self, node):
		if node == self.max:			#has no successor
			return node.getRight()

		n = node.getRight()
		if node.getRight().getHeight() != -1:			#the node have a right son
			while n.getLeft().getHeight() != -1: 		#search of the first node that dont have a left son, O(logn)
				n = n.getLeft()
			return n
		else:											#the node have no right son
			n = node
			while n.getParent().getLeft() != n: 		#search of the first node that is a left parent, O(logn)
				n = n.getParent()
			return n.getParent()

	"""returns the predecessor of a given node,WC - O(logn)

	@rtype: int
	@returns: the predecessor of the node, virtual node if has no predecessor
	"""
	def Predecessor(self, node):
		if node == self.min:			# has no Predecessor
			return node.getLeft()

		n = node.getLeft()
		if node.getLeft().getHeight() != -1:		#the node have a left son
			while n.getRight().getHeight() != -1:  	#search of the first node that dont have a right son, O(logn)
				n=n.getRight()
			return n
		else:										#the node have no left son
			n = node
			while n.getParent().getRight() != n:  	#search of the first node that is a right parent, O(logn)
				n = n.getParent()
			return n.getParent()

	""" maintance the fields of the tree from a node up to the root, returns the sum of changes, O(logn)
	
	@rtype: int
	@returns: the number of height changes that were made
	"""
	def rebalancing(self, node):
		cnt = 0
		h = max(node.getLeft().getHeight(), node.getRight().getHeight()) + 1    # computes only for the node itself
		s = node.getLeft().getSize() + 1 + node.getRight().getSize()
		if h != node.getHeight():												# height is changed
			cnt += 1
		node.setHeight(h)
		node.size = s

		while node.getParent().getHeight() != -1:           # computes for all ancestors, O(logn)
			node = node.getParent()
			h = max(node.getLeft().getHeight(), node.getRight().getHeight()) + 1   		# h is height value
			s = node.getLeft().getSize() + 1 + node.getRight().getSize()				# s is size value
			if h != node.getHeight():											# height is changed
				cnt += 1
			node.setHeight(h)
			node.size = s

		return cnt

	""" computes the balance factor of a given node
	
	@rtype: int
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
			B.getParent().setLeft(B)
		elif direction == 'R':
			B.getParent().setRight(B)
		else:
			self.root = B
		self.virtualNode.virtualInit()
		self.rebalancing(C)
		return

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
			B.getParent().setLeft(B)
		elif direction == 'R':
			B.getParent().setRight(B)
		else:
			self.root = B
		self.virtualNode.virtualInit()
		self.rebalancing(C)
		return

	""" left then right rotation (BF = +2 and BF OF LEFT SON = -1)

           C                               C                         B
             /    Left Right Rotation        /                         / \
         A       - - - - - - - >         B       - - - - - - - >   A   C
          \                             /                                   
           B                           A                                 

    """
	def left_right_rotation(self, C):
		self.left_rotation(C.getLeft())  ## rotation left of A,B
		self.right_rotation(C)  ## rotation right of B, C
		return

	""" right then left rotation (BF = -2 and BF OF RIGHT SON = +1)

           A                               A                             B
               \    Right Left Rotation        \                           / \
             C     - - - - - - - >           B       - - - - - - - >   A   C
            /                                 \                                   
           B                                   C                          

    """
	def right_left_rotation(self, A):
		self.right_rotation(A.getRight())  ## rotation right of B, C
		self.left_rotation(A)  ## rotation left of A, B
		return

	""" the function check if the tree need rotations, from the specific node to the root, and return the number of balancing actions
    """
	def is_Rotation(self, node):

		cnt = 0
		while node.getHeight() != -1:

			bf = self.balancefactor(node)  ## check the balance factor of the node

			## if the bf is OK continue to the parent until u reach to the root
			if (abs(bf) < 2):
				node = node.getParent()

			## the bf is not OK, so do one of the rotations
			else:
				if (bf == -2):
					if ((self.balancefactor(node.getRight())) == -1 or (self.balancefactor(node.getRight())) == 0):
						## bf of right son is -1
						self.left_rotation(node)
						cnt += 1
					else:
						## bf of right son is +1
						self.right_left_rotation(node)
						cnt += 2
				elif (bf == 2):
					if (self.balancefactor(node.getLeft()) == 1) or (self.balancefactor(node.getLeft()) == 0):
						## bf of left son is +1
						self.right_rotation(node)
						cnt += 1
					else:
						## bf of left son is -1
						self.left_right_rotation(node)
						cnt += 2
				node = node.getParent()
		return cnt

	def join(self, x, tree2):

		tree1 = self

		if self.root.getSize() == 0:
			tree2.insert(0, x.getValue())

			tree2.rebalancing(x)
			tree2.is_Rotation(x)
			tree2.rebalancing(x)
			return tree2

		if tree2.root.getSize() == 0:
			tree1.insert(tree1.root.getSize(), x.getValue())

			tree1.rebalancing(x)
			tree1.is_Rotation(x)
			tree1.rebalancing(x)
			return tree1


		if tree1.getRoot().getHeight() == tree2.getRoot().getHeight():
			tree = AVLTreeList()
			tree.root = x
			tree.root.setLeft(tree1.getRoot())
			tree.root.setRight(tree2.getRoot())
			tree.rebalancing(x)

			return tree

		if tree1.getRoot().getHeight() < tree2.getRoot().getHeight():
			height = tree1.root.getHeight()
			spine_node = tree2.spine(height, 'L')
			spine_parent = spine_node.getParent()
			tree1.root.setParent(x)
			x.setLeft(tree1.root)
			spine_node.setParent(x)
			x.setRight(spine_node)
			x.setParent(spine_parent)
			spine_parent.setLeft(x)

			tree2.rebalancing(x)
			tree2.is_Rotation(x)
			tree2.rebalancing(x)

			return tree2

		if tree1.getRoot().getHeight() > tree2.getRoot().getHeight():
			height = tree2.root.getHeight()
			spine_node = tree1.spine(height, 'R')
			spine_parent = spine_node.getParent()
			tree2.root.setParent(x)
			x.setRight(tree2.root)
			spine_node.setParent(x)
			x.setLeft(spine_node)
			x.setParent(spine_parent)
			spine_parent.setRight(x)

			tree1.rebalancing(x)
			tree1.is_Rotation(x)
			tree1.rebalancing(x)

			return tree1

		return None

	def get_min(self):
		node = self.root
		while node.getLeft().getHeight() != -1:
			node = node.getLeft()
		return node

	def get_max(self):
		node = self.root
		while node.getRight().getHeight() != -1:
			node = node.getRight()
		return node

	def spine(self, h, direct):
		node = self.root
		if direct == 'R':
			while node.getHeight() > h:
				node = node.getRight()
		else:
			while node.getHeight() > h:
				node = node.getLeft()
		return node

###############################
##### from here only repr #####
###############################
	"for tester only"
	def append(self, val):
		return self.insert(self.length(), val)

	def getTreeHeight(self):
		return self.root.getHeight()

	"""prints out the tree
	"""
	def __repr__(self):  # no need to understand the implementation of this one
		out = ""
		for row in self.printree(self.root):  # need printree.py file
			out = out + row + "\n"
		return out

	""" the function print the first n elements in the tree
	"""
	def print_Tree(self, n):
		for i in range(n):
			t = tree.retrieveNode(i)
			print("")
			print("        Parent " + t.getParent().getValue())
			print("           |")
			print("         Node " + t.getValue())
			print("      /         \\")
			print("left son " + t.getLeft().getValue() + "     right son " + t.getRight().getValue())
			print("")
		return

	def printree(self, t, bykey=False):
		"""Print a textual representation of t
        bykey=True: show keys instead of values"""
		# for row in trepr(t, bykey):
		#        print(row)
		return self.trepr(t, bykey)

	def trepr(self, t, bykey=False):
		"""Return a list of textual representations of the levels in t
        bykey=True: show keys instead of values"""
		if t.getHeight() == -1:
			return ["#"]

		thistr = str(t.value)

		return self.conc(self.trepr(t.left, bykey), thistr, self.trepr(t.right, bykey))

	def conc(self, left, root, right):
		"""Return a concatenation of textual represantations of
        a root node, its left node, and its right node
        root is a string, and left and right are lists of strings"""

		lwid = len(left[-1])
		rwid = len(right[-1])
		rootwid = len(root)

		result = [(lwid + 1) * " " + root + (rwid + 1) * " "]

		ls = self.leftspace(left[0])
		rs = self.rightspace(right[0])
		result.append(ls * " " + (lwid - ls) * "_" + "/" + rootwid * " " + "\\" + rs * "_" + (rwid - rs) * " ")

		for i in range(max(len(left), len(right))):
			row = ""
			if i < len(left):
				row += left[i]
			else:
				row += lwid * " "

			row += (rootwid + 2) * " "

			if i < len(right):
				row += right[i]
			else:
				row += rwid * " "

			result.append(row)

		return result

	def leftspace(self, row):
		"""helper for conc"""
		# row is the first row of a left node
		# returns the index of where the second whitespace starts
		i = len(row) - 1
		while row[i] == " ":
			i -= 1
		return i + 1

	def rightspace(self, row):
		"""helper for conc"""
		# row is the first row of a right node
		# returns the index of where the first whitespace ends
		i = 0
		while row[i] == " ":
			i += 1
		return i