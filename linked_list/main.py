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
        self.start = None
        self.end = self.start
        self.elements = elements or []
        self.current_node = self.start
        self.linked_list = []

        for elem in self.elements:
            self.linked_list.append(elem)
        
        if self.linked_list:
            self.start = self.linked_list[0]
            self.end = self.linked_list[-1]

        # size_of_elements = len(self.elements)
        # for i, elem in enumerate(self.elements, start=1):
        #     self.current_node = Node(elem)
        #     if i == size_of_elements:
        #         self.end = self.current_node
        #         break
            
        #     if not self.start:
        #         self.start = Node(elem)
        #         self.current_node.next = Node(self.elements[i])
        #         self.start.next = self.current_node.next
                
        #     if not self.current_node.next:
        #         # self.current_node = Node(self.elements[i])
        #         # self.current_node.next = Node(self.elements[i])
        #         self.current_node = Node(elem)
        #         self.current_node.next = self.current_node
        
        # try:
        #     pass
        
        # except StopIteration:
        #     self.current_node = Node(elem)
        #     self.end = self.current_node
        
        # iterate through elements
        # create a node for each elem in elements with elem as its value and
        # declared as the previous self.next
        # self.current_node = self.start
        # for i, elem in enumerate(elements):
        #     self.current_node = Node(elem)
        #     self.current_node.next = i+1
            
    def __str__(self):
        return str(self)

    def __len__(self):
        count = 0
        if self.start is None:
            return 0
        else:
            self.current_node = self.start
            
        while next(self.current_node):
            count += 1
            self.current_node = next(self.current_node)
        return count

    def __iter__(self):
        for node in self.linked_list:
            yield node

    def __getitem__(self, index):
        return self

    def __add__(self, other):
        return self + other

    def __iadd__(self, other):
        return self + other

    def __eq__(self, other):

            self.current_node = self.start
            other.current_node = other.start

            while self.current_node.next == other.current_node.next:
                if self.current_node == other.current_node:
                    self.current_node = self.current_node.next
                    other.current_node = other.current_node.next

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
        try:
            self.pop(index)
        except Exception:
            raise IndexError