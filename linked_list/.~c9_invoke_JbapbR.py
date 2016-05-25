class AbstractLinkedList(object):
    """
    Abstract class representing the LinkedList inteface you must respect.
    
    You must not implement any of the method in this class, and this class
    must never be instantiated. It's just a "guide" of which methods
    the LinkedList class should respect.
    """

    def __str__(self):
        raise NotImplementedError()

    def __len__(self):
        raise NotImplementedError()

    def __iter__(self):
        raise NotImplementedError()

    def __getitem__(self, index):
        raise NotImplementedError()

    def __add__(self, other):
        raise NotImplementedError()

    def __iadd__(self, other):
        raise NotImplementedError()

    def __eq__(self, other):
        raise NotImplementedError()

    def append(self, element):
        raise NotImplementedError()

    def count(self):
        raise NotImplementedError()

    def pop(self, index=None):
        raise NotImplementedError()


class Node(object):
    """
    Node class representing each of the linked nodes in the list.
    """

    def __init__(self, elem, next=None):
        self.elem = elem
        self.next = next

    def __str__(self):
        return str(self.elem)

    def __eq__(self, other):
        return self.elem == other.elem

    def __repr__(self):
        return repr(self.elem)


class LinkedList(AbstractLinkedList):
    """
    Implementation of an AbstractLinkedList inteface.
    """

    def __init__(self, elements=None):
        if not elements:
            self.elements = []
        else:
            self.elements = elements
        
        self.start = self.elements[0]
        self.end = self.elements[-1]
        
        for elem in elements:
            elem = Node(elem)
            self.elements.append(elem)

    def __str__(self):
        return str(self.elements)

    def __len__(self):
        return len(self.elements)

    def __iter__(self):
        return next(self.elements)

    def __getitem__(self, index):
        return self.elements[index]

    def __add__(self, other):
        return self.elements + other.elements

            pass
        return self.elements + other.elements

    def __eq__(self, other):
        try:
            return self.elements == other.elements
        except AttributeError:
            pass

    def append(self, elem):
        return self.elements.append(elem)

    def count(self):
        return len(self)

    def pop(self, index=None):
        if index:
            return self.pop(index)
