import unittest
from queue.Queue import Queue


class NodeSpec(unittest.TestCase):
    def test_create(self):
        queue = Queue()
        self.assertIsNotNone(queue)

    def test_en_queue(self):
        queue = Queue()
        self.assertEqual(queue.enQueue(20), 20)
        self.assertEqual(queue.data[0], 20)

    def test_de_queue(self):
        queue = Queue()
        queue.enQueue(2)
        self.assertEqual(queue.deQueue(), 2)
        self.assertIsNone(queue.deQueue())
        queue.enQueue(3)
        queue.enQueue(4)
        queue.enQueue(5)
        queue.enQueue(6)
        self.assertEqual(queue.deQueue(), 6)
        self.assertEqual(queue.deQueue(), 5)
        self.assertEqual(queue.deQueue(), 4)
        self.assertEqual(queue.deQueue(), 3)
        self.assertIsNone(queue.deQueue())


if __name__ == '__main__':
    unittest.main()
