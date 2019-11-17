'''
Evercise # 3: Using the find_successor method, write a non-recursive inorder traversal for a binary
search tree. 
Answer: Look at function nonrecinorder()

Evercise # 4: Modify the code for a binary search tree to make it threaded. Write a non-recursive
inorder traversal method for the threaded binary search tree. A threaded binary tree
maintains a reference from each node to its successor.
Answer: Look at function nonrecinorderwithsuccessorprop()

Evercise # 5: Modify our implementation of the binary search tree so that it handles duplicate 
keys properly. That is, if a key is already in the tree then the new payload should replace the 
old rather than add another node with the same key.
Answer: Updated put() method and _put() method to override value and not increase size property
'''

class BinarySearchTree:
    """Binary Seach Tree Class

    Interface:
        put(key,val)
        __setitem__(k,v)
        get(key)
        __getitem__(key)
        __contains__(key)
        length()
        __len__()
        __iter__()
        delete(key)
        __delitem__(key)
        remove(node)
        inorder()
        nonrecinorder()
        nonrecinorderwithsuccessorprop()
        postorder()
        preorder()
    """

    def __init__(self):
        self.__root = None
        self.__size = 0
    
    @property
    def root(self):
        return self.__root

    @property
    def size(self):
        return self.__size

    @root.setter
    def root(self,newroot):
        """ root property setter
        Arguments: newroot {Object} - Node
        """
        self.__root = newroot

    @size.setter
    def size(self,newsize):
        """ size property setter
        Arguments: newsize {Int}
        """
        self.__size = newsize
    
    def put(self,key,val):
        """Puts key value into BST
        Arguments:
            key {Object} -- key to access value
            val {Object} -- value
        """
        #replacing value
        if not key in self:
            self.size +=  1
        if self.root:
            self._put(key,val,self.root)
        else:
            self.root = TreeNode(key,val)

    def _put(self,key,val,currentNode):
        """Helper method for put() when not updating root
        Arguments:
            key {Object} -- key to access value
            val {Object} -- value
        """
        if key == currentNode.key:
            currentNode.payload = val
        elif key < currentNode.key:
            if currentNode.hasLeftChild():
                self._put(key,val,currentNode.leftChild)
            else:
                currentNode.leftChild = TreeNode(key,val,parent=currentNode,successor=currentNode)
        else:
            if currentNode.hasRightChild():
                self._put(key,val,currentNode.rightChild)
            else:
                currentNode.rightChild = TreeNode(key,val,parent=currentNode,successor=currentNode.successor)
                currentNode.successor = currentNode.rightChild

            
    def __setitem__(self,k,v):
        """Overridding dunder method for put to use bracket notation
        EX: bst[key] = value
        Arguments:
            key {Object} -- key to access value
            val {Object} -- value
        """
        self.put(k,v)

    def get(self,key):
        """Method to get item value using key
        Arguments:
            key {Object} -- key to access value
        Returns:
            val {Object} -- value
        """
        if self.root:
            res = self._get(key,self.root)
            if res:
                return res.payload
            else:
                return None
        else:
            return None
        
    def _get(self,key,currentNode):
        """Helper method for get() when not getting from root
        Arguments:
            key {Object} -- key to access value
            currentNode {Node}
        Returns:
            val {Object} -- value
        """
        if not currentNode:
            return None
        elif currentNode.key == key:
            return currentNode
        elif key < currentNode.key:
            return self._get(key,currentNode.leftChild)
        else:
            return self._get(key,currentNode.rightChild)
            
        
    def __getitem__(self,key):
        """Overridding dunder method for get to use bracket notation
        EX: x = bst[key]
        Arguments:
            key {Object} -- key to access value
        Returns:
            val {Object} -- value
        """
        res = self.get(key)
        if res:
            return res
        else:
            raise KeyError('Error, key not in tree')
            

    def __contains__(self,key):
        """Overridding dunder method to use 'in' syntax
        EX: x in bst
        Arguments:
            key {Object} -- key to access value
        Returns:
            {Boolean}
        """
        if self._get(key,self.root):
            return True
        else:
            return False
        
    def length(self):
        """Returns size of search tree"""
        return self.size

    def __len__(self):
        """
        Overriddes dunder len method to use len syntax
        EX: len(bst)
        """
        return self.size

    def __iter__(self):
        """Overriddes dunder iter method to allow iteration over objects in class
        """
        return self.root.__iter__()
    
    def delete(self,key):
        """Deletes Node with key match from BST
        Arguments:
            key {Object} -- key
        """
        if self.size > 1:
            nodeToRemove = self._get(key,self.root)
            if nodeToRemove:
                self.remove(nodeToRemove)
                self.size = self.size-1
            else:
                raise KeyError('Error, key not in tree')
        elif self.size == 1 and self.root.key == key:
            self.root = None
            self.size = self.size - 1
        else:
            raise KeyError('Error, key not in tree')

    def __delitem__(self,key):
        """Overriddes dunder del method to allow del syntax
        EX: del bst[x]
        """
        self.delete(key)
    
    def remove(self,currentNode):
        """Helper method for delete method to remove node from tree
        Arguments:
            currentNode {TreeNode}
        """
        if currentNode.isLeaf(): #leaf
            if currentNode == currentNode.parent.leftChild:
                currentNode.parent.leftChild = None
            else:
                currentNode.parent.rightChild = None
                currentNode.parent.successor = currentNode.parent.findSuccessor()
        elif currentNode.hasBothChildren(): #interior
            succ = currentNode.findSuccessor()
            succ.spliceOut()
            currentNode.key = succ.key
            currentNode.payload = succ.payload
            currentNode.successor = succ.successor
        else: # this node has one child
            if currentNode.hasLeftChild():
                if currentNode.isLeftChild():
                    currentNode.leftChild.parent = currentNode.parent
                    currentNode.parent.leftChild = currentNode.leftChild
                elif currentNode.isRightChild():
                    currentNode.leftChild.parent = currentNode.parent
                    currentNode.parent.rightChild = currentNode.leftChild
                    currentNode.parent.successor = currentNode.leftChild
                else: #root
                    if currentNode.leftChild.successor ==  currentNode:
                        currentNode.leftChild.successor =  None 

                    currentNode.replaceNodeData(currentNode.leftChild.key,
                                       currentNode.leftChild.payload,
                                       currentNode.leftChild.leftChild,
                                       currentNode.leftChild.rightChild,
                                       currentNode.leftChild.successor)
            else: #has only right child
                if currentNode.isLeftChild():
                    currentNode.rightChild.parent = currentNode.parent
                    currentNode.parent.leftChild = currentNode.rightChild
                elif currentNode.isRightChild():
                    currentNode.rightChild.parent = currentNode.parent
                    currentNode.parent.rightChild = currentNode.rightChild
                    currentNode.parent.successor = currentNode.rightChild
                else: #root
                    
                    currentNode.replaceNodeData(currentNode.rightChild.key, #key
                                       currentNode.rightChild.payload, #value
                                       currentNode.rightChild.leftChild, #left child
                                       currentNode.rightChild.rightChild,#right child
                                       currentNode.rightChild.successor) 


    def inorder(self):
        """Runs in order traversal on Tree"""
        self._inorder(self.root)

    def _inorder(self,tree):
        """Runs in order traversal on Tree"""
        if tree != None:
            self._inorder(tree.leftChild)
            print(tree.key)
            self._inorder(tree.rightChild)

    def nonrecinorder(self):
        """Non recursive in order traversal on Tree"""
        tree = self.root
        visited = []
        while tree != None:

            if tree.hasLeftChild() and tree.leftChild.key not in visited:
                tree = tree.leftChild

            else: #tree.leftChild == None or tree == self.root or tree.leftChild.key in visited:
                visited.append(tree.key)
                print(tree.key)
                tree = tree.findSuccessor()

        # return value for testing purposes only
        return visited
    
    def nonrecinorderwithsuccessorprop(self):
        """Non recursive in order traversal on Tree using successor property"""
        tree = self.root
        visited = []
        while tree != None:
            #has left child and has not been visited
            if tree.hasLeftChild() and tree.leftChild.key not in visited:
                tree = tree.leftChild

            else: 
                visited.append(tree.key)
                print(tree.key)
                tree = tree.successor

        # return value for testing purposes only
        return visited       

    def postorder(self):
        """Runs post order traversal on Tree"""
        self._postorder(self.root)

    def _postorder(self, tree):
        """Runs post order traversal on Tree"""
        if tree:
            self._postorder(tree.rightChild)
            self._postorder(tree.leftChild)
            print(tree.key)            

    def preorder(self):
        """Runs pre order traversal on Tree"""
        self._preorder(self,self.root)

    def _preorder(self,tree):
        """Runs pre order traversal on Tree"""
        if tree:
            print(tree.key)            
            self._preorder(tree.leftChild)
            self._preorder(tree.rightChild)

                
class TreeNode:
    """Tree Node Class
        Interface:
            hasLeftChild()
            hasRightChild()
            isLeftChild()
            isRightChild()
            isRoot()
            isLeaf()
            hasAnyChildren()
            hasBothChildren()
            replaceNodeData(key,value,leftchild,rightchild,successor)
            findSuccessor()
            spliceOut()
            findMin()
            __iter__()
    """    
    def __init__(self,key,val,left=None,right=None,parent=None,successor=None):
        self.key = key
        self.payload = val
        self.leftChild = left
        self.rightChild = right
        self.parent = parent
        self.successor = successor
        self.balanceFactor = 0
        
    def hasLeftChild(self):
        """Looks to see if node has left child
        Returns:
            {Boolean}
        """
        return self.leftChild

    def hasRightChild(self):
        """Looks to see if node has right child
        Returns:
            {Boolean}
        """
        return self.rightChild
    
    def isLeftChild(self):
        """Looks to see if node is left child
        Returns:
            {Boolean}
        """
        return self.parent and self.parent.leftChild == self

    def isRightChild(self):
        """Looks to see if node is right child
        Returns:
            {Boolean}
        """
        return self.parent and self.parent.rightChild == self

    def isRoot(self):
        """Looks to see if node is root
        Returns:
            {Boolean}
        """
        return not self.parent

    def isLeaf(self):
        """Looks to see if node has no children
        Returns:
            {Boolean}
        """
        return not (self.rightChild or self.leftChild)

    def hasAnyChildren(self):
        """Looks to see if node has any children
        Returns:
            {Boolean}
        """
        return self.rightChild or self.leftChild

    def hasBothChildren(self):
        """Looks to see if node has both children
        Returns:
            {Boolean}
        """
        return self.rightChild and self.leftChild
    
    def replaceNodeData(self,key,value,lc,rc,sc):
        """Replaces data in node
        Arguments:
            key {Object} -- key
            value {Object} -- value
            lc {TreeNode} -- left child
            rc {TreeNode} -- right child
            sc {TreeNode} -- successor node
        """
        self.key = key
        self.payload = value
        self.leftChild = lc
        self.rightChild = rc
        self.successor = sc
        if self.hasLeftChild():
            self.leftChild.parent = self
            self.leftChild.successor = self
        if self.hasRightChild():
            self.rightChild.parent = self
        
    def findSuccessor(self):
        """Finds successor to Tree Node
        Returns:
            {Tree Node} -- successor
        """
        succ = None
        if self.hasRightChild():
            succ = self.rightChild.findMin()
        else:
            if self.parent:
                if self.isLeftChild():
                    succ = self.parent
                else:
                    self.parent.rightChild = None
                    succ = self.parent.findSuccessor()
                    self.parent.rightChild = self
        return succ

    def nonrecfindsuccessor(self):
        if self.hasRightChild():
            return self.rightChild.findMin()
        else:
            parent = self.parent
            while parent is not None:
                if self != parent.rightChild:
                    break
                self = parent
                parent = parent.parent
        return parent

    def spliceOut(self):
        """Removes Tree Node from BST """
        if self.isLeaf():
            if self.isLeftChild():
                self.parent.leftChild = None
            else:
                self.parent.rightChild = None
                self.parent.successor = self.parent.findSuccessor()
        elif self.hasAnyChildren():
            if self.hasLeftChild():
                if self.isLeftChild():
                    self.parent.leftChild = self.leftChild
                    self.leftChild.successor = self.parent
                else:
                    self.parent.rightChild = self.leftChild
                    self.parent.successor = self.leftChild
                self.leftChild.parent = self.parent
                self.leftChild.successor = self.leftChild.findSuccessor()
                
            else: #has right child
                if self.isLeftChild():
                    self.parent.leftChild = self.rightChild
                    #
                else: #is right child
                    self.parent.rightChild = self.rightChild
                    self.parent.successor = self.rightChild
                self.rightChild.parent = self.parent

    def findMin(self):
        """Finds lowest node on left tree"""
        current = self
        while current.hasLeftChild():
            current = current.leftChild
        return current

    def __iter__(self):
        """The standard inorder traversal of a binary tree."""
        if self:
            if self.hasLeftChild():
                for elem in self.leftChild: #recursively goes down left child
                    yield elem
            yield self.key
            if self.hasRightChild():
                for elem in self.rightChild: #recursively goes down right child
                    yield elem