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


        # self.end = self.start

        # self.start = Node(elements[0])
        self.end = self.start
        
        self.elements = elements
        
        size_of_elements = len(elements)
        for i, elem in enumerate(self.elements, start=1):
            current_node = Node(elem)
            if i > size_of_elements:
                self.end = current_node
                break
            if not self.start:
                self.start = current_node
            if not current_node.next:
                current_node = current_node.next
        
        try:
            pass
        
        except StopIteration:
            current_node = Node(elem)
            self.end = current_node
        
        # iterate through elements
        # create a node for each elem in elements with elem as its value and
        # declared as the previous self.next
        current_node = self.start
        for i, elem in enumerate(elements):
            current_node = Node(elem)
            current_node.next = i+1
            
    def __str__(self):
        return str(self.elements)

        self.start = node

    def __len__(self):
        return len(self.elements)

    def __iter__(self):
        return next(self.elements)

    def __getitem__(self, index):
        return self.elements[index]

    def __add__(self, other):
        return self.elements + other.elements

    def __iadd__(self, other):
        return self.elements + other.elements

    def __eq__(self, other):
        try:
            return self.elements == other.elements
        except AttributeError:
            pass

    def append(self, elem):
        if self.start is None:
            self.start = Node(elem)
            self.end = self.start
        else:
            self.end.next = Node(elem)
            self.end = self.end.next
            


    def count(self):
        return len(self)

    def pop(self, index=None):
        if index:
            return self.pop(index)
