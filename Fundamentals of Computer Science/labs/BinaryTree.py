# Linnea Wennberg, grudat24 uppg 2.5

import random

class _Node:
    """Private class that creates a node in the tree"""
    def __init__(self, data=None, right=None, left=None): # Time complexity O(1), only assigns values
        self._data = data
        self._right = right
        self._left = left
        self._prio = random.randint(1, 10000)
        
class BinaryTree:
    """Creates an empty tree"""
    def __init__(self): # Time complexity O(1), only assigns values
        self._root = None
        self._size = 0

    def insert(self, data): # Time complexity O(1), only assigns values
        """Inserts a new node in the tree"""
        if type(data) is str:
            if self._root == None:
                self._root = _Node(data)
                self._size += 1
            else:
                node = _Node(data)
                self._root = addElement(self._root, node)
                self._size += 1
        else:
           return "Input must be string!"

    def _rotateRight(self, tree): # Time complexity O(1), only re-assigns values
        """Rotates the tree to the right"""
        newtree = tree._left
        node = newtree._right
        newtree._right = tree
        tree._left = node
        return newtree
    
    def _rotateLeft(self, tree): # Time complexity O(1), only re-assigns values
        """Rotates the tree to the left"""
        newtree = tree._right
        node = newtree._left
        newtree._left = tree
        tree._right = node
        return newtree

    def length(self): # Time complexity O(1), only accesses and returns a single value
        """Returns the number of elements in this list"""
        return self._size

    def _order(self, node, list):  # Time complexity O(n) since it accesses all the elements in the tree
        """Help function to add the elements of tree to a string and returns a list of the elements"""
        if node == None:
            return node
        self._order(node._left, list)
        list.append(node._data)
        self._order(node._right, list)
        return list

    def string(self): # Time complexity O(n), since it has to go through all elements in the tree
        """Returns a string of the elements of the tree in alphabetical order"""
        if self._root == None:
            return "The tree is empty."
        else:
            list = []
            string = self._order(self._root, list)
            string = ", ".join(string)
            return string
            

def addElement(tree, node): # Time complexity O(logn), since it doesn't access all elements
    """Function that adds a new element to the tree, balances it and returns the new tree"""
    if tree == None:
        return node
    if node._data < tree._data:
        tree._left = addElement(tree._left, node)
        if tree._prio > tree._left._prio:
            tree = BinaryTree()._rotateRight(tree)
    else:
        tree._right = addElement(tree._right, node)
        if tree._prio > tree._right._prio:
            tree = BinaryTree()._rotateLeft(tree)
    return tree

def prioTest(tree): # Time complexity O(n), since it has to go through all elements in the tree
    """Test to check that the priority of each element is correct"""
    if tree:
        if tree._right:
            assert tree._prio < tree._right._prio 
            assert tree._data < tree._right._data
            prioTest(tree._right)
        if tree._left:
            assert tree._prio < tree._left._prio 
            assert tree._data > tree._left._data
            prioTest(tree._left)
    return True

def main():
    tree = BinaryTree()
    assert tree.string() == "The tree is empty."
    assert prioTest(tree._root)
    assert tree.length() == 0
    tree.insert("Kiwi")
    tree.insert("Banana")
    assert tree.string() == "Banana, Kiwi"
    assert prioTest(tree._root)
    tree.insert("Apple")
    tree.insert("Peach")
    assert tree.insert(3) == "Input must be string!"
    tree.insert("Orange")
    tree.insert("Pear")
    tree.insert("Grapes")
    assert tree.length() == 7
    assert tree.string() == "Apple, Banana, Grapes, Kiwi, Orange, Peach, Pear"
    assert prioTest(tree._root)
    tree.insert("Starfruit")
    assert prioTest(tree._root)
    assert tree.string() == "Apple, Banana, Grapes, Kiwi, Orange, Peach, Pear, Starfruit"


main()

