"""
Singly Linked List implementation.

Supports: push, pop, top, len, is_empty, find, remove.
Reads integers from a text file.
"""


class Node:
    """A single node in the linked list."""

    def __init__(self, value):
        self.value = value
        self.next = None


class SinglyLinkedList:
    """
    A singly linked list that stores integers.

    All operations work with the head of the list.
    The list is built without any external modules.
    """

    def __init__(self):
        self._head = None
        self._size = 0

    def push(self, x):
        """
        Insert a new element x at the beginning of the list.
        Time complexity: O(1).
        """
        new_node = Node(x)
        new_node.next = self._head
        self._head = new_node
        self._size += 1

    def pop(self):
        """
        Remove and return the element at the head of the list.
        Raises IndexError if the list is empty.
        Time complexity: O(1).
        """
        if self._head is None:
            raise IndexError("pop from an empty list")

        value = self._head.value
        self._head = self._head.next
        self._size -= 1
        return value

    def top(self):
        """
        Return the value at the head without removing it.
        Raises IndexError if the list is empty.
        Time complexity: O(1).
        """
        if self._head is None:
            raise IndexError("top from an empty list")

        return self._head.value

    def len(self):
        """
        Return the number of elements currently in the list.
        Time complexity: O(1).
        """
        return self._size

    def is_empty(self):
        """
        Return True if the list contains no elements, False otherwise.
        Time complexity: O(1).
        """
        return self._size == 0

    def find(self, x):
        """
        Search for a node containing value x.
        Returns True if found, False otherwise.
        Time complexity: O(n).
        """
        current = self._head
        while current is not None:
            if current.value == x:
                return True
            current = current.next
        return False

    def remove(self, x):
        """
        Remove the first occurrence of value x from the list.
        Returns True if the element was found and removed, False otherwise.
        Time complexity: O(n).
        """
        if self._head is None:
            return False

        if self._head.value == x:
            self._head = self._head.next
            self._size -= 1
            return True

        previous = self._head
        current = self._head.next
        while current is not None:
            if current.value == x:
                previous.next = current.next
                self._size -= 1
                return True
            previous = current
            current = current.next

        return False

    @classmethod
    def from_file(cls, filepath):
        """
        Create a SinglyLinkedList by reading integers from a text file.
        Each line must contain exactly one integer.
        Elements are pushed in the order they appear in the file,
        so the last line ends up at the head.
        """
        linked_list = cls()
        with open(filepath, "r") as file:
            for line in file:
                line = line.strip()
                if line:
                    linked_list.push(int(line))
        return linked_list

    def __repr__(self):
        """Return a readable string showing the list contents head → tail."""
        elements = []
        current = self._head
        while current is not None:
            elements.append(str(current.value))
            current = current.next
        return "HEAD -> " + " -> ".join(elements) + " -> None"

if __name__ == "__main__":
    lst = SinglyLinkedList()

    print("=== Basic operations ===")
    lst.push(10)
    lst.push(20)
    lst.push(30)
    print(lst)

    print("top()   :", lst.top())
    print("pop()   :", lst.pop())
    print("len()   :", lst.len())
    print("is_empty:", lst.is_empty())
    print(lst)

    print("\n=== find / remove ===")
    print("find(10):", lst.find(10))
    print("find(99):", lst.find(99))

    print("remove(10):", lst.remove(10))
    print("remove(99):", lst.remove(99))
    print(lst)

    print("\n=== Edge cases ===")
    lst2 = SinglyLinkedList()
    print("is_empty:", lst2.is_empty())
    print("find(1) :", lst2.find(1))
    print("remove(1):", lst2.remove(1))

    try:
        lst2.pop()
    except IndexError as e:
        print("pop() on empty list raised IndexError:", e)

    try:
        lst2.top()
    except IndexError as e:
        print("top() on empty list raised IndexError:", e)

    print("\n=== Single-element list ===")
    lst3 = SinglyLinkedList()
    lst3.push(42)
    print(lst3)
    print("remove(42):", lst3.remove(42))
    print(lst3)
    print("is_empty:", lst3.is_empty())