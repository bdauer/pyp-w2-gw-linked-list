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
        
        # todo: format nicely.
        
        return str(self.elem)

    def __eq__(self, other):
        
        #Todo: check that other is a node.
        
        return self.elem == other.elem

    def __repr__(self):
        
        # todo: format nicely.
        return str(self.elem)


class LinkedList(AbstractLinkedList):
    """
    Implementation of an AbstractLinkedList inteface.
    """

    def __init__(self, elements=None):
        
        # Address an elements=None case according to spec.
        self.start = None
        self.end = None


        # create a linked list out of the provided elements.
        if elements:
            for elem in elements:
                self.append(elem)
            
    def __str__(self):
        return str(self)

    def __len__(self):
        
        return sum(1 for i in self)
        
    def __iter__(self):
        
        # begin generator at the first node.
        current_node = self.start
        while current_node:
            # yield the current node and reassign to the linked node.
            yield current_node
            current_node = current_node.next

    def __getitem__(self, index):
        
        # iterate through the linked list and return node at index.
        
        for i, node in enumerate(self):
            if i == index:
                return node

    def __add__(self, other):
        
        # todo
        return self + other

    def __iadd__(self, other):
        
        #todo
        return self + other

    def __eq__(self, other):

        current_node_s = self.start
        current_node_o = other.start

        while current_node_s.next and current_node_o.next:
            if current_node_s == current_node_o:
                current_node_s = current_node_s.next
                current_node_o = current_node_o.next
            else:
                pass
        
        return self == other

    def append(self, elem):
        
        
        # instantiate a new node.
        current_node = Node(elem)

        # if there is no first node, create one.
        if not self.start:
            self.start = current_node
        
        # if there is a last node, point it at the new node.        
        if self.end:
            self.end.next = current_node
            
        # assign the newly created node as the last node.        
        self.end = current_node
        
        # The above works better because it treats constructing the linked list
        # as repeatedly appending nodes.

        # if self.start is None:
        #     self.start = Node(elem)
        #     self.end = self.start
        # else:
        #     self.end.next = Node(elem)
        #     self.end = self.end.next

    def count(self):
        return len(self)

    def pop(self, index=None):
        
        # todo
        
        try:
            pass
        except Exception:
            raise IndexError