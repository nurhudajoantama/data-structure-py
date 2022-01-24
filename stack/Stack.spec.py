from inspect import stack
import unittest
from Stack import Stack


class NodeSpec(unittest.TestCase):

    def test_create(self):
        stack = Stack()
        self.assertIsNotNone(stack)

    def test_append(self):
        stack = Stack()
        stack.append(1)
        self.assertEqual(stack.data[0], 1)
        self.assertEqual(stack.append(2), 2)
        self.assertEqual(stack.data[1], 2)

    def test_pop(self):
        stack = Stack()
        stack.append(1)
        pop_res = stack.pop()
        self.assertEqual(pop_res, 1)

    def test_error_pop(self):
        stack = Stack()
        self.assertIsNone(stack.pop())

    def test_multiple_action(self):
        stack = Stack()
        self.assertEqual(stack.append(1), 1)
        self.assertEqual(stack.append(2), 2)
        self.assertEqual(stack.append(3), 3)
        self.assertEqual(stack.pop(), 3)
        self.assertEqual(stack.pop(), 2)
        self.assertEqual(stack.pop(), 1)
        self.assertIsNone(stack.pop())


if __name__ == '__main__':
    unittest.main()
