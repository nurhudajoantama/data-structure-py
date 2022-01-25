import unittest
from linked_list.LinkedList import LinkedList


class LinkedListSpec(unittest.TestCase):

    def test_create(self):
        linkList = LinkedList()
        self.assertIsNotNone(linkList)
        self.assertIsNone(linkList.head)

    def test_push(self):
        linkList = LinkedList()
        linkList.push(5)
        linkList.push(6)
        linkList.push(7)
        self.assertEqual(linkList.head.data, 7)
        self.assertEqual(linkList.head.next.data, 6)
        self.assertEqual(linkList.head.next.next.data, 5)

    def test_read_at(self):
        linkList = LinkedList()
        linkList.push(1)
        linkList.push(2)
        self.assertEqual(linkList.read(1), 1)
        self.assertIsNone(linkList.read(20))

    def test_append(self):
        linkList = LinkedList()
        linkList.append(1)
        linkList.append(2)
        linkList.append(3)
        linkList.append(4)
        self.assertEqual(linkList.read(0), 1)
        self.assertEqual(linkList.read(1), 2)
        self.assertEqual(linkList.read(3), 4)

    def test_pop(self):
        linkList = LinkedList()
        linkList.append(1)
        self.assertEqual(linkList.read(0), 1)
        linkList.pop()
        self.assertIsNone(linkList.read(0))
        linkList.append(1)
        linkList.append(2)
        linkList.append(3)
        linkList.pop()
        self.assertIsNone(linkList.read(2))

    def test_insert_at(self):
        linkList = LinkedList()
        linkList.insertAt(0, 1)
        linkList.insertAt(1, 12)
        self.assertEqual(linkList.read(0), 1)
        self.assertEqual(linkList.read(1), 12)
        linkList.insertAt(0, 14)
        self.assertEqual(linkList.read(0), 14)

    def test_error_insert_at(self):
        linkList = LinkedList()
        linkList.insertAt(0, 1)
        with self.assertRaises(Exception) as context:
            linkList.insertAt(20, 2)
        self.assertTrue('linked list not sufficient' in str(context.exception))
        self.assertEqual(linkList.read(0), 1)
        self.assertIsNone(linkList.read(1))

    def test_remove_at_head(self):
        linkList = LinkedList()
        linkList.append(1)
        linkList.append(2)
        self.assertEqual(linkList.read(0), 1)
        linkList.removeAt(0)
        self.assertEqual(linkList.read(0), 2)

    def test_remove_at(self):
        linkList = LinkedList()
        linkList.append(1)
        linkList.append(2)
        linkList.append(3)
        linkList.append(4)
        self.assertEqual(linkList.read(1), 2)
        linkList.removeAt(1)
        self.assertEqual(linkList.read(1), 3)
        linkList.removeAt(2)
        self.assertIsNone(linkList.read(2))

    def test_error_remove(self):
        linkList = LinkedList()
        with self.assertRaises(Exception) as context:
            linkList.removeAt(0)
        self.assertTrue('Not have an data' in str(context.exception))
        linkList.append(1)
        linkList.append(2)
        linkList.append(3)
        with self.assertRaises(Exception) as context:
            linkList.removeAt(3)
        self.assertTrue('Not have an data' in str(context.exception))


if __name__ == '__main__':
    unittest.main()
