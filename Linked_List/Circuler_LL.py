# Create a Linked List and Traverse and Display all elements
class _Node:
    __slots__ = '_element', '_next'

    def __init__(self, element, next):
        self._element = element
        self._next = next


class CircularList:
    def __init__(self):
        self._head = None
        self._tail = None
        self._size = 0

    def __len__(self):
        return self._size

    def isempty(self):
        return self._size == 0

    def add(self, e):
        newest = _Node(e, None)
        if self.isempty():
            newest._next = newest
            self._head = newest
        else:
            newest._next = self._tail._next
            self._tail._next = newest
        self._tail = newest
        self._size += 1

    def display(self):
        p = self._head
        i = 0
        while i < len(self):
            print(p._element, end="-->")
            p = p._next
            i = i+1
        print()


L = CircularList()
L.add(1)
L.add(2)
L.add(3)
L.add(4)
L.add(5)
L.add(6)
L.display()
print("Size:", len(L))
