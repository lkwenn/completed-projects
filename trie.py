# Linnea Wennberg, grudat24 slutprojekt

"""
Library implementing a trie, a tree-like structure to store a set of strings as a tree of characters. 
Each node in the tree, apart from the root, represents a letter of the alphabet. 
A word in the tree is located by traversing a branch the tree. 
This implementation uses the English alphabet (A-Z) and does not support special characters.
"""

class Node:
    def __init__(self, word:str=None):
        """
        Creates a new node object in the Trie.
        """
        self._children = {}
        self._is_end = False


class Trie:
    def __init__(self):
        """
        Creates a new, empty Trie object.
        """
        self._root = Node()
        self._size = 0
    

    def insert(self, word: str):
        """
        Inserts a new given string into the Trie.
        """
        if not word or not isinstance(word, str) or not word.isalpha():
            raise TypeError("Input can only be a string containing letters")
        current = self._root
        for letter in word:
            if letter not in current._children:
                current._children[letter] = Node()
            current = current._children[letter]
        current._is_end = True
        self._size += 1


    def search(self, word: str) -> bool:
        """
        Returns True if given string exists in the Trie. Returns False if string does not exist.
        """
        if not word or not isinstance(word, str) or not word.isalpha():
            raise TypeError("Input can only be a string containing letters")
        if self._size == 0:
            return False
        current = self._root
        for letter in word:
            node = current._children.get(letter)
            if not node: # If letter is not in trie
                return False
            current = node
        return current._is_end


    def _starts_with(self, current, prefix):
        """
        Help function that returns a list of the words starting with a given string (prefix).
        Uses recursion to traverse the branch from the end point to the start of the word.
        """
        words = []
        if current._is_end:
            words.append(prefix)
        for letter in current._children.keys():
            words.extend(self._starts_with(current._children[letter], prefix+letter))
        return words


    def starts_with(self, prefix: str) -> str:
        """
        Returns a list with all the words starting with a given string (prefix). 
        Returns False if none exist.
        """
        if not prefix or not isinstance(prefix, str) or not prefix.isalpha():
            raise TypeError("Input can only be a string containing letters")
        if self._size == 0:
            return False
        current = self._root
        for letter in prefix:
            if letter in current._children.keys():
                current = current._children[letter]
            else:
                return False
        return self._starts_with(current, prefix)


    def delete(self, word: str) -> bool:
        """
        Removes a given string from the Trie. Returns True if string exists and has been deleted, 
        returns False if string isn't in the Trie.
        """
        if not word or not isinstance(word, str) or not word.isalpha():
            raise TypeError("Input can only be a string containing letters")
        if self._size == 0:
            return False
        current = self._root
        for letter in word:
            if letter in current._children.keys():
                current = current._children[letter]
            else:
                return False
        current._is_end = False
        self._size -= 1
        return True


    def get_all(self, node=None) -> str:
        """
        Returns a string of all the words in the Trie.
        """
        if self._size == 0:
            return None
        all_list = []
        current = self._root
        for node in current._children:
            prefix_list = self.starts_with(node)
            all_list.extend(prefix_list)
        all = ", ".join(all_list)
        return all


    def size(self) -> int:
        """
        Returns the number of words in the Trie.
        """
        return self._size
    