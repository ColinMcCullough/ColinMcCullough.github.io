class BinaryTree:
    def __init__(self,rootObj):
        self.key = rootObj
        self.leftChild = None
        self.rightChild = None

    def insertLeft(self,newNode):
        oldleft = self.leftChild
        self.leftChild = BinaryTree(newNode)
        self.leftChild.leftChild = oldleft

    def insertRight(self,newNode):
        oldright = self.rightChild
        self.rightChild = BinaryTree(newNode)
        self.rightChild.rightChild = oldright

    def getRightChild(self):
        return self.rightChild

    def getLeftChild(self):
        return self.leftChild

    def setRootVal(self,obj):
        self.key = obj

    def getRootVal(self):
        return self.key
'''
def buildtree():
    t = BinaryTree('a')
    t.insertLeft('b')
    t.insertRight('c')
    t.getLeftChild().insertRight('d')
    t.getRightChild().insertRight('f')
    t.getRightChild().insertLeft('e')
    return t

x = buildtree()
print(x.getRightChild().getRootVal())
print(x.getLeftChild().getRightChild().getRootVal())
print(x.getRightChild().getLeftChild().getRootVal())

['(', '3', '+', '(', '4', '*', '5' ,')',')']
'''