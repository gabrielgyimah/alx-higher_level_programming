#!/usr/bin/python3

"""Create a new template of type Node."""


class Node:
    """Create a new template of type Node."""

    def __init__(self, data=0, next_node=None):
        """Initializes the current Node"""
        if not isinstance(data, int):
            raise TypeError("data must be an integer")

        if next_node is not None and not isinstance(next_node, Node):
            raise TypeError("next_node must be a Node object")
        self.__data = data
        self.__next_node = next_node

    @property
    def data(self):
        """Returns the data of the current node"""
        return self.__data

    @data.setter
    def data(self, value):
        """Setter for the current node"""
        if not isinstance(value, int):
            raise TypeError("data must be an integer")
        self.__data = value

    @property
    def next_node(self):
        """Returns the address of the next node"""
        return self.__next_node

    @next_node.setter
    def next_node(self, value):
        """Sets the next node for the current node"""
        if value is not None and not isinstance(value, Node):
            raise TypeError("next_node must be a Node object")
        self.__next_node = value


"""Create an instance of the class SinglyLinkedList."""


class SinglyLinkedList:
    """Create an instance of the class SinglyLinkedList."""

    def __init__(self):
        """Initializes instances of the class SinglyLinkedList."""
        self.__head = None

    def __str__(self):
        """Print str representation of singlelinkedlist."""
        tmp = self.__head
        out = ''
        while tmp:
            out += str(tmp.data)
            out += '\n'
            tmp = tmp.next_node
        return out[:len(out) - 1]

    def sorted_insert(self, value):
        """Insert in a sorted order"""
        node = Node(value)
        if not self.__head:
            self.__head = node
        elif self.__head.data > value:
            node.next_node = self.__head
            self.__head = node
        else:
            h = self.__head

            while h.next_node and h.next_node.data < value:
                h = h.next_node
            node.next_node = h.next_node
            h.next_node = node
