# Create a Linked List and Traverse and Display all elements

# Crating a Node using class
class _Node:
    __slots__ = '_element', '_next'

    def __init__(self, element, next):
        self._element = element
        self._next = next


class LinkedList:
    def __init__(self):
        self._head = None
        self._tail = None
        self._size = 0

    def __len__(self):
        return self._size

    def isempty(self):
        return self._size == 0

    def addlast(self, e):
        newest = _Node(e, None)
        if self.isempty():
            self._head = newest
        else:
            self._tail._next = newest
        self._tail = newest
        self._size += 1

    def display(self):
        p = self._head
        while p:
            print(p._element, end='-->')
            p = p._next
        print()

# using this method we can add any element to any location
    def AddElement(self, e, position):
        newest = _Node(e, None)
        p = self._head
        i = 1
        while i < position-1:
            p = p._next
            i = i+1
        newest._next = p._next
        p._next = newest
        self._size += 1


L = LinkedList()
L.addlast(1)
L.addlast(2)
L.addlast(3)
L.display()
print("Size:", len(L))
L.AddElement(20, 4)
L.display()
print("Size:", len(L))
