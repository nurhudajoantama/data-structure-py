import unittest
from double_linked_list.DoubleLinkedList import DoubleLinkedList


class NodeSpec(unittest.TestCase):
    def test_create(self):
        dll = DoubleLinkedList()
        self.assertIsNotNone(dll)

    def test_multiple_append_read(self):
        dll = DoubleLinkedList()
        dll.append(10)
        dll.append(11)
        dll.append(12)
        dll.append(13)
        dll.append(14)
        dll.append(15)
        self.assertEqual(dll.read(5), 15)
        self.assertEqual(dll.read(4), 14)
        self.assertEqual(dll.read(3), 13)
        self.assertEqual(dll.read(2), 12)
        self.assertEqual(dll.read(1), 11)
        self.assertEqual(dll.read(0), 10)

    def test_multiple_insert_read_middle(self):
        dll = DoubleLinkedList()
        dll.append(10)
        dll.append(11)
        dll.append(12)
        dll.append(13)
        dll.append(14)
        dll.append(15)
        dll.insert(5, 20)
        dll.insert(6, 25)
        self.assertEqual(dll.read(5), 20)

    def test_tail_after_inser_head(self):
        dll = DoubleLinkedList()
        dll.insert(0, 10)
        dll.insert(0, 11)
        self.assertEqual(dll.tail.prev.data, 11)

    def test_tail_insert_in_head(self):
        dll = DoubleLinkedList()
        dll.insert(0, 10)
        dll.insert(0, 11)
        dll.insert(2, 9)
        dll.insert(3, 8)
        self.assertEqual(dll.read(0), 11)
        self.assertEqual(dll.read(1), 10)
        self.assertEqual(dll.read(2), 9)
        self.assertEqual(dll.read(3), 8)


if __name__ == '__main__':
    unittest.main()
