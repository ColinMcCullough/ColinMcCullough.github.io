from priorityqueue import *
import unittest

class PriorityQueueTests(unittest.TestCase):

    def setUp(self):
        self.queue = PriorityQueue()
    
    def test_enqueue_decueue(self):
        self.queue.enqueue(100)
        self.queue.enqueue(50)
        self.queue.enqueue(10)
        self.queue.enqueue(20)
        self.queue.enqueue(30)
        self.queue.enqueue(15)
        self.assertEqual(self.queue.dequeue(),10)
        self.assertEqual(self.queue.dequeue(),15)
        self.assertEqual(self.queue.dequeue(),20)
        self.assertEqual(self.queue.dequeue(),30)
        self.assertEqual(self.queue.dequeue(),50)
        self.assertEqual(self.queue.dequeue(),100)
        with self.assertRaises(IndexError):
            self.queue.dequeue()

    


if __name__ == '__main__':
    unittest.main()







    