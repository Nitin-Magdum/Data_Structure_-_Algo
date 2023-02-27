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

    def Search(self,key):
        p= self._head
        index=0
        while p:
            if (p._element==key):
                return index
            p=p._next
            index+=1
        return


L = LinkedList()
L.addlast(1)
L.addlast(2)
L.addlast(3)
L.addlast(4)
L.addlast(5)
L.addlast(6)
L.addlast(7)
L.addlast(8)
L.addlast(9)
L.addlast(10)
L.display()
print("Size:", len(L))
i=L.Search(10)
print("Search Element is on position:",i)
