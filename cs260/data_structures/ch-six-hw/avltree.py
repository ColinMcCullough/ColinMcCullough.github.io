from binarysearchtree import BinarySearchTree, TreeNode
import unittest

class AVLTree(BinarySearchTree):
    """AVL Balanced Binary Search Tree,
    Inherits from Binary Search Tree Class
    Overrides the following Binary Search Tree Class Methods:
        _put(key,val)
        remove(key)
    Arguments:
        BinarySearchTree {BinarySearchTree}
    """    
    def __init__(self):
        BinarySearchTree.__init__(self)

    

    def _put(self,key,val,currentNode):
        """Puts key value into AVL Tree
        Arguments:
            key {Object} -- key to access value
            val {Object} -- value
        """
        #replaces value if matching
        if key == currentNode.key:
            currentNode.payload = val
        elif key < currentNode.key:
            if currentNode.hasLeftChild():
                self._put(key,val,currentNode.leftChild)
            else:
                currentNode.leftChild = TreeNode(key,val,parent=currentNode,successor=currentNode)
                self.update_ancestor_successors(currentNode)
                self.updateBalance(currentNode.leftChild,'add')
        else:
            if currentNode.hasRightChild():
                self._put(key,val,currentNode.rightChild)
            else:
                currentNode.rightChild = TreeNode(key,val,parent=currentNode,successor=currentNode.successor)
                currentNode.successor = currentNode.rightChild
                self.updateBalance(currentNode.rightChild,'add')

    def remove(self,currentNode):
        """Helper method for delete method to remove node from tree
        Arguments:
            currentNode {TreeNode}
        """
        if currentNode.isLeaf(): #leaf
            if currentNode == currentNode.parent.leftChild:
                currentNode.parent.leftChild = None
                currentNode.parent.balanceFactor -= 1
                self.updateBalance(currentNode.parent,'del')
            else:
                currentNode.parent.rightChild = None
                currentNode.parent.successor = currentNode.parent.findSuccessor()
                currentNode.parent.balanceFactor += 1
                self.updateBalance(currentNode.parent,'del')
        elif currentNode.hasBothChildren(): #interior
            succ = currentNode.findSuccessor()
            succ.spliceOut()
            currentNode.key = succ.key
            currentNode.payload = succ.payload
            currentNode.successor = succ.successor
            currentNode.balanceFactor += 1
            self.updateBalance(currentNode.parent,'del')
        else: # this node has one child
            if currentNode.hasLeftChild():
                if currentNode.isLeftChild():
                    currentNode.leftChild.parent = currentNode.parent
                    currentNode.parent.leftChild = currentNode.leftChild
                    currentNode.leftChild.successor = currentNode.parent
                    currentNode.parent.balanceFactor -= 1
                    self.updateBalance(currentNode.parent,'del')
                elif currentNode.isRightChild():
                    currentNode.leftChild.parent = currentNode.parent
                    currentNode.parent.rightChild = currentNode.leftChild
                    currentNode.parent.successor = currentNode.leftChild
                    currentNode.leftChild.successor = currentNode.leftChild.findSuccessor()
                    currentNode.parent.balanceFactor += 1
                    self.updateBalance(currentNode.parent,'del')
                else: #root
                    if currentNode.leftChild.successor ==  currentNode:
                        currentNode.leftChild.successor =  None 
                    currentNode.balanceFactor -= 1
                    currentNode.replaceNodeData(currentNode.leftChild.key,
                                       currentNode.leftChild.payload,
                                       currentNode.leftChild.leftChild,
                                       currentNode.leftChild.rightChild,
                                       currentNode.leftChild.successor)
            else: #has only right child
                if currentNode.isLeftChild():
                    currentNode.rightChild.parent = currentNode.parent
                    currentNode.parent.leftChild = currentNode.rightChild
                    currentNode.parent.balanceFactor -= 1
                    self.update_ancestor_successors(currentNode.parent)
                    self.updateBalance(currentNode.parent,'del')
                elif currentNode.isRightChild():
                    currentNode.rightChild.parent = currentNode.parent
                    currentNode.parent.rightChild = currentNode.rightChild
                    currentNode.parent.successor = currentNode.rightChild
                    currentNode.parent.balanceFactor += 1
                    self.updateBalance(currentNode.parent,'del')
                else: #root
                    currentNode.balanceFactor += 1
                    currentNode.replaceNodeData(currentNode.rightChild.key, #key
                                       currentNode.rightChild.payload, #value
                                       currentNode.rightChild.leftChild, #left child
                                       currentNode.rightChild.rightChild,#right child
                                       currentNode.rightChild.successor)                
    
    def updateBalance(self,node,caller):
        """Updates balance property of node based on
           left subtree - right subtree
        Arguments:
            node {TreeNode} -- a Tree Node
        """      
        if node.balanceFactor > 1 or node.balanceFactor < -1:
            self.rebalance(node)
            return
        if node.parent != None:
            if node.isLeftChild():
                if caller == 'add':
                    node.parent.balanceFactor += 1
                else:
                    node.parent.balanceFactor -= 1
            elif node.isRightChild():
                if caller == 'add':
                    node.parent.balanceFactor -= 1
                else: 
                    node.parent.balanceFactor += 1
            if node.parent.balanceFactor != 0:
                self.updateBalance(node.parent,caller)

    def rebalance(self,node):
        """Rebalances node that is out of balance
        Arguments:
            node {TreeNode} -- a Tree Node
        """        
        if node.balanceFactor < 0:
            if node.rightChild.balanceFactor > 0:
                # Do an LR Rotation
                self.rotateRight(node.rightChild)
                self.rotateLeft(node)
            else:
                # single left
                self.rotateLeft(node)
        elif node.balanceFactor > 0:
            if node.leftChild.balanceFactor < 0:
                # Do an RL Rotation
                self.rotateLeft(node.leftChild)
                self.rotateRight(node)
            else:
                # single right
                self.rotateRight(node)

    def rotateLeft(self,rotRoot):
        """Rotates root to the left
           and updates references
        Arguments:
            rotRoot {TreeNode} -- root that will be rotated
        """        
        newRoot = rotRoot.rightChild
        rotRoot.rightChild = newRoot.leftChild
        if newRoot.leftChild != None:
            newRoot.leftChild.parent = rotRoot
        newRoot.parent = rotRoot.parent
        if rotRoot.isRoot():
            self.root = newRoot
        else:
            if rotRoot.isLeftChild():
                rotRoot.parent.leftChild = newRoot
            else:
                rotRoot.parent.rightChild = newRoot
        newRoot.leftChild = rotRoot
        rotRoot.parent = newRoot
        rotRoot.balanceFactor = rotRoot.balanceFactor + 1 - min(newRoot.balanceFactor, 0)
        newRoot.balanceFactor = newRoot.balanceFactor + 1 + max(rotRoot.balanceFactor, 0)


    def rotateRight(self,rotRoot):
        """Rotates root to the right
           and updates references
        Arguments:
            rotRoot {TreeNode} -- root that will be rotated
        """  
        newRoot = rotRoot.leftChild
        rotRoot.leftChild = newRoot.rightChild
        if newRoot.rightChild != None:
            newRoot.rightChild.parent = rotRoot
        newRoot.parent = rotRoot.parent
        if rotRoot.isRoot():
            self.root = newRoot
        else:
            if rotRoot.isRightChild():
                rotRoot.parent.rightChild = newRoot
            else:
                rotRoot.parent.leftChild = newRoot
        newRoot.rightChild = rotRoot
        rotRoot.parent = newRoot
        rotRoot.balanceFactor = rotRoot.balanceFactor - 1 - max(newRoot.balanceFactor, 0)
        newRoot.balanceFactor = newRoot.balanceFactor - 1 + min(rotRoot.balanceFactor, 0)