import unittest
from tree.Node import Node


class NodeSpec(unittest.TestCase):

    def test_create_node(self):
        node = Node(1)
        self.assertIsNotNone(node)

    def test_insert_data(self):
        node = Node(12)
        self.assertEqual(node.data, 12)

    def test_child(self):
        node = Node(1)
        node.addChild(2)
        node.addChild(3)
        self.assertEqual(node.child[0].data, 2)
        self.assertEqual(node.child[1].data, 3)


if __name__ == '__main__':
    unittest.main()
