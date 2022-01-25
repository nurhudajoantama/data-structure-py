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
        node2 = Node(2)
        node3 = Node(3)
        node.child.append(node2)
        node.child.append(node3)
        self.assertEqual(node.child[0], node2)
        self.assertEqual(node.child[1], node3)


if __name__ == '__main__':
    unittest.main()
