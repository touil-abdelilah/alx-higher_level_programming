#!/usr/bin/python3
"""SinglyLinkedList module"""


class Node:
    """Class that defines a node of a singly linked list."""

    def __init__(self, data, next_node=None):
        """Initialization method with data and next_node."""
        self.data = data
        self.next_node = next_node

    @property
    def data(self):
        """Getter method to retrieve the data."""
        return self.__data

    @data.setter
    def data(self, value):
        """Setter method to set the data."""
        if not isinstance(value, int):
            raise TypeError("data must be an integer")
        else:
            self.__data = value

    @property
    def next_node(self):
        """Getter method to retrieve the next_node."""
        return self.__next_node

    @next_node.setter
    def next_node(self, value):
        """Setter method to set the next_node."""
        if value is not None and not isinstance(value, Node):
            raise TypeError("next_node must be a Node object")
        else:
            self.__next_node = value


class SinglyLinkedList:
    """Class that defines a singly linked list."""
    def __init__(self):
        """Simple instantiation method."""
        self.head = None

    def sorted_insert(self, value):
        """Method to insert a new Node into the correct sorted position."""
        new_node = Node(value)

        if self.head is None or value < self.head.data:
            new_node.next_node = self.head
            self.head = new_node
            return

        current = self.head
        while current.next_node is not None and current.next_node.data < value:
            current = current.next_node

        new_node.next_node = current.next_node
        current.next_node = new_node

    def __str__(self):
        """Method to print the entire list in stdout."""
        result = ""
        current = self.head
        while current:
            result += str(current.data) + "\n"
            current = current.next_node
        return result.strip()
