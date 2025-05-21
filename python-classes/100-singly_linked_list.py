#!/usr/bin/python3
"""
100-singly_linked_list.py
Module containing class Node.
"""


class Node:
    """
    A class to define a node.
    """
    def __init__(self, data, next_node=None):
        """
        Initializes an new node.

        Parameters:
        data (int): data of the node
        next_node (Node):
        """
        if not isinstance(data, int):
            raise TypeError("data must be an integer")
        else:
            self.__data = data
        if not isinstance(next_node, Node) and next_node is not None:
            raise TypeError("next_node must be a Node object")
        else:
            self.__next_node = next_node

    @property
    def data(self):
        """
        Gets the data of the node.
        """
        return self.__data

    @data.setter
    def data(self, value):
        """
        Sets the data of the node.
        """
        if not isinstance(value, int):
            raise TypeError("data must be an integer")
        else:
            self.__data = value

    @property
    def next_node(self):
        """
        Gets the next_node.
        """
        return self.__next_node

    @next_node.setter
    def next_node(self, value):
        """
        Sets the next_node.
        """
        if not isinstance(value, Node) and next_node is not None:
            raise TypeError("next_node must be a Node object")
        else:
            self.__next_node = value


class SinglyLinkedList:
    """
    A class to define a singly linked list.
    """
    def __init__(self):
        """
        Initializes a new singly linked list.
        """
        self.__head = None

    def __str__(self):
        """
        Prints each node of the list.
        """
        collection = ""
        current = self.__head
        while current is not None:
            collection += str(current.data)
            if current.next_node is not None:
                collection += "\n"
            current = current.next_node
        return collection

    def sorted_insert(self, value):
        """
        Inserts a new node in the correct position.
        """
        new = Node(value)
        if self.__head is None:
            self.__head = new
        elif self.__head.data > value:
            new.next_node = self.__head
            self.__head = new
        else:
            current = self.__head
            while current.next_node is not None:
                if current.next_node.data > value:
                    break
                else:
                    current = current.next_node
            if current.next_node is None:
                current.next_node = new
            else:
                new.next_node = current.next_node
                current.next_node = new
