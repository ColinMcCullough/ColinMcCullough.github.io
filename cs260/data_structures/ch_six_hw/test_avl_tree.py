import unittest
from avltree import *
class AVLTreeTests(unittest.TestCase):
    def setUp(self):
        self.bst = AVLTree()

    def test_put_1(self):
        self.bst.put(30,'a')
        self.bst.put(50,'b')
        #right rotate then left rotate
        self.bst.put(40,'c')
        #check node placements
        assert self.bst.root.key == 40
        assert self.bst.root.rightChild.key == 50
        assert self.bst.root.leftChild.key == 30
        #check successors
        assert self.bst.root.successor.key == 50
        assert self.bst.root.rightChild.successor == None
        assert self.bst.root.leftChild.successor.key == 40
        #check balance factors
        assert self.bst.root.balanceFactor == 0
        assert self.bst.root.rightChild.balanceFactor == 0
        assert self.bst.root.leftChild.balanceFactor == 0

    def test_put_2(self):
        self.bst.put(30,'a')
        self.bst.put(10,'b')
         #left rotate then right rotate
        self.bst.put(20,'c')
        #check node placements
        assert self.bst.root.key == 20
        assert self.bst.root.rightChild.key == 30
        assert self.bst.root.leftChild.key == 10
        #check successors
        assert self.bst.root.successor.key == 30
        assert self.bst.root.rightChild.successor == None
        assert self.bst.root.leftChild.successor.key == 20
        #check balance factors
        assert self.bst.root.balanceFactor == 0
        assert self.bst.root.rightChild.balanceFactor == 0
        assert self.bst.root.leftChild.balanceFactor == 0

    def test_put_3(self):
        self.bst.put(50,'a')
        self.bst.put(30,'b')
        self.bst.put(70,'c')
        self.bst.put(80,'c')
        self.bst.put(60,'d')
        #left rotate
        self.bst.put(90,'e')
        #check node placements
        assert self.bst.root.key == 70
        assert self.bst.root.rightChild.key == 80
        assert self.bst.root.rightChild.rightChild.key == 90
        assert self.bst.root.leftChild.key == 50
        assert self.bst.root.leftChild.rightChild.key == 60
        assert self.bst.root.leftChild.leftChild.key == 30
        #check successors
        assert self.bst.root.successor.key == 80
        assert self.bst.root.rightChild.successor.key == 90
        assert self.bst.root.rightChild.rightChild.successor == None
        assert self.bst.root.leftChild.successor.key == 60
        assert self.bst.root.leftChild.rightChild.successor.key == 70
        assert self.bst.root.leftChild.leftChild.successor.key == 50
        #check balance factors
        assert self.bst.root.balanceFactor == 0
        assert self.bst.root.rightChild.balanceFactor == -1
        assert self.bst.root.rightChild.rightChild.balanceFactor == 0
        assert self.bst.root.leftChild.balanceFactor == 0
        assert self.bst.root.leftChild.rightChild.balanceFactor == 0
        assert self.bst.root.leftChild.leftChild.balanceFactor == 0

    def test_put_4(self):
        self.bst.put(40,'a')
        self.bst.put(30,'b')
        self.bst.put(50,'c')
        self.bst.put(45,'d')
        self.bst.put(60,'e')
        #right rotate then left rotate
        self.bst.put(43,'f')
        #check node placements
        assert self.bst.root.key == 45
        assert self.bst.root.rightChild.key == 50
        assert self.bst.root.rightChild.rightChild.key == 60
        assert self.bst.root.leftChild.key == 40
        assert self.bst.root.leftChild.rightChild.key == 43
        assert self.bst.root.leftChild.leftChild.key == 30
        #check successors
        assert self.bst.root.successor.key == 50
        assert self.bst.root.rightChild.successor.key == 60
        assert self.bst.root.rightChild.rightChild.successor == None
        assert self.bst.root.leftChild.successor.key == 43
        assert self.bst.root.leftChild.rightChild.successor.key == 45
        assert self.bst.root.leftChild.leftChild.successor.key == 40
        #check balance factors
        assert self.bst.root.balanceFactor == 0
        assert self.bst.root.rightChild.balanceFactor == -1
        assert self.bst.root.rightChild.rightChild.balanceFactor == 0
        assert self.bst.root.leftChild.balanceFactor == 0
        assert self.bst.root.leftChild.rightChild.balanceFactor == 0
        assert self.bst.root.leftChild.leftChild.balanceFactor == 0

    def test_put_5(self):
        self.bst.put(40,'a')
        self.bst.put(30,'b')
        self.bst.put(50,'c')
        self.bst.put(10,'d')
        self.bst.put(35,'e')
        #left rotate then right rotate
        self.bst.put(37,'f')
        #check node placements
        assert self.bst.root.key == 35
        assert self.bst.root.rightChild.key == 40
        assert self.bst.root.rightChild.rightChild.key == 50
        assert self.bst.root.rightChild.leftChild.key == 37
        assert self.bst.root.leftChild.key == 30
        assert self.bst.root.leftChild.leftChild.key == 10
        #check successors
        assert self.bst.root.successor.key == 37
        assert self.bst.root.rightChild.successor.key == 50
        assert self.bst.root.rightChild.rightChild.successor == None
        assert self.bst.root.rightChild.leftChild.successor.key == 40
        assert self.bst.root.leftChild.successor.key == 35
        assert self.bst.root.leftChild.leftChild.successor.key == 30
        #check balance factors
        assert self.bst.root.balanceFactor == 0
        assert self.bst.root.rightChild.balanceFactor == 0
        assert self.bst.root.rightChild.rightChild.balanceFactor == 0
        assert self.bst.root.rightChild.leftChild.balanceFactor == 0
        assert self.bst.root.leftChild.balanceFactor == 1
        assert self.bst.root.leftChild.leftChild.balanceFactor == 0
        
    def test_put_6(self):
        self.bst.put(30,'a')
        self.bst.put(20,'b')
        #right rotate
        self.bst.put(10,'c')
        #check node placements
        assert self.bst.root.key == 20
        assert self.bst.root.rightChild.key == 30
        assert self.bst.root.leftChild.key == 10
        #check successors
        assert self.bst.root.successor.key == 30
        assert self.bst.root.rightChild.successor == None
        assert self.bst.root.leftChild.successor.key == 20
        #check balance factors
        assert self.bst.root.balanceFactor == 0
        assert self.bst.root.rightChild.balanceFactor == 0
        assert self.bst.root.leftChild.balanceFactor == 0

    def test_remove_1(self):
        #no rotations, remove left leaf
        self.bst.put(10,'a')
        self.bst.put(20,'b')
        self.bst.put(5,'c')
        self.bst.delete(5)
        #check node placements
        assert self.bst.root.key == 10
        assert self.bst.root.rightChild.key == 20
        assert self.bst.root.leftChild == None
        #check successors
        assert self.bst.root.successor.key == 20
        assert self.bst.root.rightChild.successor == None
        #check balance factors
        assert self.bst.root.balanceFactor == -1
        assert self.bst.root.rightChild.balanceFactor == 0

    def test_remove_2(self):
        #no rotations, remove right leaf
        self.bst.put(10,'a')
        self.bst.put(20,'b')
        self.bst.put(5,'c')
        self.bst.delete(20)
        #check node placements
        assert self.bst.root.key == 10
        assert self.bst.root.rightChild == None
        assert self.bst.root.leftChild.key == 5
        #check successors
        assert self.bst.root.successor == None
        assert self.bst.root.leftChild.successor.key == 10
        #check balance factors
        assert self.bst.root.balanceFactor == 1
        assert self.bst.root.leftChild.balanceFactor == 0

    def test_remove_3(self):
        #remove node with both children is right child
        self.bst.put(10,'a')
        self.bst.put(20,'a')
        self.bst.put(5,'a')
        self.bst.put(4,'a')
        self.bst.put(17,'a')
        self.bst.put(22,'a')
        self.bst.delete(20)
        #check node placements
        assert self.bst.root.key == 10
        assert self.bst.root.rightChild.key == 22
        assert self.bst.root.rightChild.leftChild.key == 17
        assert self.bst.root.leftChild.key == 5
        assert self.bst.root.leftChild.leftChild.key == 4
        #check successors
        assert self.bst.root.successor.key == 17
        assert self.bst.root.rightChild.successor == None
        assert self.bst.root.rightChild.leftChild.successor.key == 22
        assert self.bst.root.leftChild.successor.key == 10
        assert self.bst.root.leftChild.leftChild.successor.key == 5
        #check balance factors
        assert self.bst.root.balanceFactor == 0
        assert self.bst.root.rightChild.balanceFactor == 1
        assert self.bst.root.rightChild.leftChild.balanceFactor == 0
        assert self.bst.root.leftChild.balanceFactor == 1
        assert self.bst.root.leftChild.leftChild.balanceFactor == 0

    def test_remove_4(self):
        #right rotation with delete
        self.bst.put(10,'a')
        self.bst.put(20,'b')
        self.bst.put(5,'c')
        self.bst.put(4,'c')
        self.bst.delete(20)
        #check node placements
        assert self.bst.root.key == 5
        assert self.bst.root.rightChild.key == 10
        assert self.bst.root.leftChild.key == 4
        #check successors
        assert self.bst.root.successor.key == 10
        assert self.bst.root.rightChild.successor == None
        assert self.bst.root.leftChild.successor.key == 5
        #check balance factors
        assert self.bst.root.balanceFactor == 0
        assert self.bst.root.leftChild.balanceFactor == 0
        assert self.bst.root.rightChild.balanceFactor == 0

    def test_remove_5(self):
        #left rotation with delete
        self.bst.put(10,'a')
        self.bst.put(20,'b')
        self.bst.put(5,'c')
        self.bst.put(30,'c')
        self.bst.delete(5)
        #check node placements
        assert self.bst.root.key == 20
        assert self.bst.root.rightChild.key == 30
        assert self.bst.root.leftChild.key == 10
        #check successors
        assert self.bst.root.successor.key == 30
        assert self.bst.root.rightChild.successor == None
        assert self.bst.root.leftChild.successor.key == 20
        #check balance factors
        assert self.bst.root.balanceFactor == 0
        assert self.bst.root.leftChild.balanceFactor == 0
        assert self.bst.root.rightChild.balanceFactor == 0

    def test_remove_6(self):
        #left rotation then right rotation with delete
        self.bst.put(50,'a')
        self.bst.put(40,'b')
        self.bst.put(60,'c')
        self.bst.put(70,'c')
        self.bst.put(30,'c')
        self.bst.put(45,'c')
        self.bst.put(43,'c')
        self.bst.delete(60)
        #check node placements
        assert self.bst.root.key == 45
        assert self.bst.root.leftChild.key == 40
        assert self.bst.root.leftChild.leftChild.key == 30
        assert self.bst.root.leftChild.rightChild.key == 43
        assert self.bst.root.rightChild.key == 50
        assert self.bst.root.rightChild.rightChild.key == 70
        #check successors
        assert self.bst.root.successor.key == 50
        assert self.bst.root.rightChild.successor.key == 70
        assert self.bst.root.rightChild.rightChild.successor == None
        assert self.bst.root.leftChild.successor.key == 43
        assert self.bst.root.leftChild.leftChild.successor.key == 40
        assert self.bst.root.leftChild.rightChild.successor.key == 45
        #check balance factors
        assert self.bst.root.balanceFactor == 0
        assert self.bst.root.leftChild.balanceFactor == 0
        assert self.bst.root.leftChild.leftChild.balanceFactor == 0
        assert self.bst.root.leftChild.rightChild.balanceFactor == 0
        assert self.bst.root.rightChild.balanceFactor == -1
        assert self.bst.root.rightChild.rightChild.balanceFactor == 0

    def test_remove_7(self):
        #right rotation then left rotation with delete
        self.bst.put(50,'a')
        self.bst.put(40,'b')
        self.bst.put(60,'c')
        self.bst.put(70,'c')
        self.bst.put(30,'c')
        self.bst.put(55,'c')
        self.bst.put(54,'c')
        self.bst.delete(40)
        #check node placements
        assert self.bst.root.key == 55
        assert self.bst.root.leftChild.key == 50
        assert self.bst.root.leftChild.leftChild.key == 30
        assert self.bst.root.leftChild.rightChild.key == 54
        assert self.bst.root.rightChild.key == 60
        assert self.bst.root.rightChild.rightChild.key == 70
        #check successors
        assert self.bst.root.successor.key == 60
        assert self.bst.root.rightChild.successor.key == 70
        assert self.bst.root.rightChild.rightChild.successor == None
        assert self.bst.root.leftChild.successor.key == 54
        assert self.bst.root.leftChild.leftChild.successor.key == 50
        assert self.bst.root.leftChild.rightChild.successor.key == 55
        #check balance factors
        assert self.bst.root.balanceFactor == 0
        assert self.bst.root.leftChild.balanceFactor == 0
        assert self.bst.root.leftChild.leftChild.balanceFactor == 0
        assert self.bst.root.leftChild.rightChild.balanceFactor == 0
        assert self.bst.root.rightChild.balanceFactor == -1
        assert self.bst.root.rightChild.rightChild.balanceFactor == 0

    def test_remove_8(self):
        #delete node with 1 child, has right child, is left child
        self.bst.put(50,'a')
        self.bst.put(40,'b')
        self.bst.put(60,'c')
        self.bst.put(70,'c')
        self.bst.put(30,'c')
        self.bst.put(55,'c')
        self.bst.put(57,'c')
        self.bst.delete(55)
        #check node placements
        assert self.bst.root.key == 50
        assert self.bst.root.leftChild.key == 40
        assert self.bst.root.leftChild.leftChild.key == 30
        assert self.bst.root.rightChild.key == 60
        assert self.bst.root.rightChild.rightChild.key == 70
        assert self.bst.root.rightChild.leftChild.key == 57
        #check successors
        assert self.bst.root.successor.key == 57
        assert self.bst.root.rightChild.successor.key == 70
        assert self.bst.root.rightChild.rightChild.successor == None
        assert self.bst.root.rightChild.leftChild.successor.key == 60
        assert self.bst.root.leftChild.successor.key == 50
        assert self.bst.root.leftChild.leftChild.successor.key == 40
        #check balance factors
        assert self.bst.root.balanceFactor == 0
        assert self.bst.root.leftChild.balanceFactor == 1
        assert self.bst.root.leftChild.leftChild.balanceFactor == 0
        assert self.bst.root.rightChild.leftChild.balanceFactor == 0
        assert self.bst.root.rightChild.balanceFactor == 0
        assert self.bst.root.rightChild.rightChild.balanceFactor == 0
    
    def test_remove_9(self):
        #delete node with 1 child, has right child, is right child
        self.bst.put(50,'a')
        self.bst.put(40,'b')
        self.bst.put(60,'c')
        self.bst.put(70,'c')
        self.bst.put(30,'c')
        self.bst.delete(60)
        #check node placements
        assert self.bst.root.key == 50
        assert self.bst.root.leftChild.key == 40
        assert self.bst.root.leftChild.leftChild.key == 30
        assert self.bst.root.rightChild.key == 70
        #check successors
        assert self.bst.root.successor.key == 70
        assert self.bst.root.rightChild.successor == None
        assert self.bst.root.leftChild.successor.key == 50
        assert self.bst.root.leftChild.leftChild.successor.key == 40
        #check balance factors
        assert self.bst.root.balanceFactor == 1
        assert self.bst.root.leftChild.balanceFactor == 1
        assert self.bst.root.leftChild.leftChild.balanceFactor == 0
        assert self.bst.root.rightChild.balanceFactor == 0
    
    def test_remove_10(self):
        #delete node with 1 child, has right child, is root
        self.bst.put(50,'a')
        self.bst.put(60,'b')
        self.bst.delete(50)
        #check node placements
        assert self.bst.root.key == 60
        assert self.bst.root.rightChild == None
        assert self.bst.root.successor == None
        assert self.bst.root.balanceFactor == 0
    
    def test_remove_11(self):
        #delete node with 1 child, has left child, is left child
        self.bst.put(50,'a')
        self.bst.put(60,'b')
        self.bst.put(40,'a')
        self.bst.put(30,'b')
        self.bst.put(70,'b')
        self.bst.delete(40)
        #check node placements
        assert self.bst.root.key == 50
        assert self.bst.root.leftChild.key == 30
        assert self.bst.root.rightChild.key == 60
        assert self.bst.root.rightChild.rightChild.key == 70
        #check successors
        assert self.bst.root.successor.key == 60
        assert self.bst.root.rightChild.successor.key == 70
        assert self.bst.root.rightChild.rightChild.successor == None
        assert self.bst.root.leftChild.successor.key == 50
        #check balance factors
        assert self.bst.root.balanceFactor == -1
        assert self.bst.root.leftChild.balanceFactor == 0
        assert self.bst.root.rightChild.rightChild.balanceFactor == 0
        assert self.bst.root.rightChild.balanceFactor == -1

    def test_remove_12(self):
        #delete node with 1 child, has left child, is right child
        self.bst.put(50,'a')
        self.bst.put(60,'b')
        self.bst.put(30,'b')
        self.bst.put(55,'b')
        self.bst.delete(60)
        #check node placements
        assert self.bst.root.key == 50
        assert self.bst.root.leftChild.key == 30
        assert self.bst.root.rightChild.key == 55
        #check successors
        assert self.bst.root.successor.key == 55
        assert self.bst.root.rightChild.successor == None
        assert self.bst.root.leftChild.successor.key == 50
        #check balance factors
        assert self.bst.root.balanceFactor == 0
        assert self.bst.root.leftChild.balanceFactor == 0
        assert self.bst.root.rightChild.balanceFactor == 0

    def test_remove_13(self):
        #delete node with 1 child, has left child, is root
        self.bst.put(50,'a')
        self.bst.put(40,'b')
        self.bst.delete(50)
        #check node placements
        assert self.bst.root.key == 40
        assert self.bst.root.rightChild == None
        assert self.bst.root.successor == None
        assert self.bst.root.balanceFactor == 0

if __name__ == '__main__':
    unittest.main()