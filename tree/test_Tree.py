import unittest
from tree.Tree import Tree


class TreeSpec(unittest.TestCase):

    def test_create(self):
        tree = Tree()
        self.assertIsNotNone(tree)

    def test_add_root(self):
        tree = Tree()
        tree.addRoot(1)
        self.assertEqual(tree.root.data, 1)

    def test_add_child(self):
        tree = Tree()
        tree.addRoot(1)
        tree.root.addChild(2)
        self.assertEqual(tree.root.child[0].data, 2)


if __name__ == '__main__':
    unittest.main()
