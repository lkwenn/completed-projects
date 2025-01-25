##### Linnea Wennberg, grudat24

# Trie (prefix tree)

### A tree data structure to store and locate strings in a set

A trie, also known as a prefix tree or digital tree, is a tree-like structure to store a set of strings as a tree of characters. Each node in the tree, apart from the root, represents a letter of the alphabet. A word in the tree is located by traversing a branch the tree. A trie is particularly useful to find words that start with the same prefix, for example the prefix gra- could return grape, grab, grateful and grand. Some real world applications include autocomplete, spell checker and matching algorithms.

Further reading: [Trie (Wikipedia)](https://en.wikipedia.org/wiki/Trie)


This implementation uses the English alphabet (A-Z) and does not support special characters.

### Documentation (ver 1.0.0)

#### class Node

<pre>class Node
    def __init__(self, word)</pre>

Creates a node object from a given string.\
**:param word:** _\(string)_ Word to create a new node from.

#### class Trie

<pre>class Trie
    def __init__(self)</pre>

Creates a new, empty Trie object.

#### method insert

<pre>def insert(self, word)</pre>

Inserts a new word to the trie from given string.\
**:param word:** _\(string)_ Word to be inserted.

#### method search

<pre>def search(self, word)</pre>

Searches for a word in the trie. Returns True if the word is in the trie and False if not. \
**:param word:** _\(string)_ Word to search for.\
**:return:** _\(boolean)_ True if word exists, False if the word does not exist.

#### method starts_with

<pre>def starts_with(self, prefix)</pre>

Searches and retrieves words that start with a certain prefix. If no words with the prefix exist it returns False.\
**:param prefix:** _\(string)_ Prefix to be searched.\
**:return:** _\(list)_ All the words starting with the specified prefix.
**:return:** _\(boolean)_ False if no words exist.

#### method delete

<pre>def delete(self, word)</pre>

Checks if a word is in the tree and deletes it if True.\
If the word does not exist in the tree it returns False.\
**:param word:** _\(string)_ Word to delete from Trie.\
**:return:** _\(boolean)_ True if the word is in the trie and has been deleted, False otherwise.

#### method get_all

<pre>def get_all(self)</pre>

Retrieve all the words in the trie. Returns None if trie is empty.\
**:return:** _\(string)_ All the words in the trie.

#### method size

<pre>def size(self)</pre>

Returns the number of elements in the trie.\
**:return:** _\(int)_ The total number of elements.


### Roadmap

- The API of this library is frozen.
- Version numbers adhere to semantic versioning.

The only accepted reason to modify the API is to handle issues that can't be resolved in any other reasonable way.