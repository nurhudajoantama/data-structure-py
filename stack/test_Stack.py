import unittest
from stack.Stack import Stack


class StackSpec(unittest.TestCase):

    def test_create(self):
        stack = Stack()
        self.assertIsNotNone(stack)

    def test_push(self):
        stack = Stack()
        stack.push(1)
        self.assertEqual(stack.data[0], 1)
        self.assertEqual(stack.push(2), 2)
        self.assertEqual(stack.data[1], 2)

    def test_peek(self):
        stack = Stack()
        self.assertIsNone(stack.peek())
        stack.push(1)
        self.assertEqual(stack.peek(), 1)
        self.assertEqual(stack.peek(), 1)

    def test_pop(self):
        stack = Stack()
        stack.push(1)
        pop_res = stack.pop()
        self.assertEqual(pop_res, 1)

    def test_error_pop(self):
        stack = Stack()
        self.assertIsNone(stack.pop())

    def test_multiple_action(self):
        stack = Stack()
        self.assertEqual(stack.push(1), 1)
        self.assertEqual(stack.push(2), 2)
        self.assertEqual(stack.push(3), 3)
        self.assertEqual(stack.pop(), 3)
        self.assertEqual(stack.pop(), 2)
        self.assertEqual(stack.pop(), 1)
        self.assertIsNone(stack.pop())


if __name__ == '__main__':
    unittest.main()
