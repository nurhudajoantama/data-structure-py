import unittest
from Node import Node


class NodeSpec(unittest.TestCase):

    def test_create(self):
        node = Node(None)
        self.assertIsNotNone(node)

    def test_insert_read_data(self):
        node = Node(10)
        self.assertEqual(node.data, 10)

    def test_change_data(self):
        node = Node(2)
        self.assertEqual(node.data, 2)
        node.data = 12
        self.assertEqual(node.data, 12)

    def test_insert_read_change_next(self):
        node = Node(10)
        nextNode = Node(11)
        self.assertIsNone(node.next)
        node.next = nextNode
        self.assertIsNotNone(node.next)
        self.assertEqual(node.next, nextNode)


if __name__ == '__main__':
    unittest.main()
