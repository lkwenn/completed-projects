# Linnea Wennberg, grudat24 uppg 1.2, 1.3

class ListElement: 
    """A list element that stores a value"""
    def __init__(self, data=None): # Time complexity O(1) since it doesn't depend on size of list, just assigns values
        self._data = data
        self._next = None

class LinkedList:
    """A singly linked list of elements of type T"""
    def __init__(self): # Time complexity O(1), only assigns values
        self._first = None # first element in list
        self._last = None # last element in list
        self._size = 0 # number of elements in list

    def addFirst(self, data): # Time complexity O(1), only assigns values
        """Inserts the given element at the beginning of this list."""
        newdata = ListElement(data)
        if self._first == None:
           self._first = newdata
           self._last = self._first
        else:
            newdata._next = self._first
            self._first = newdata
        self._size += 1

    def addLast(self, data): # Time complexity O(1), only assigns values
        """Inserts the given element at the end of this list."""
        newdata = ListElement(data)
        if self._first == None:
            self._first = newdata
            self._last = self._first            
        else:
            self._last._next = newdata
            self._last = newdata
        self._size += 1

    def getFirst(self): # Time complexity O(1), constant since it only accesses and returns one value
        """Returns the first element of this list. Returns none if the list is empty."""
        if self._first == None:
            return None
        else:
            return self._first._data

    def getLast(self): # Time complexity O(1), constant since it only accesses and returns one value
        """Returns the last element of this list. Returns none if the list is empty."""
        if self._first == None:
            return None
        else:
            return self._last._data

    def get(self, i): # Time complexity O(n), since it has to go through all items in the list
        """Returns the element at the specified position in this list. Returns none if index is out of bounds.
        Input should be an integer."""
        if self._first == None or self._size < i+1 or i < 0:
            return None
        else:
            index = self._first
            counter = 0
            while counter < i:
                index = index._next
                counter += 1
            return index._data


    def removeFirst(self): # Time complexity O(1), since it only reassigns values
        """Removes and returns the first element from this list. Returns none if the list is empty"""
        if self._first == None:
            return None
        elif self._size == 1:
            first = self._first._data
            self.clear()
            return first
        if self._size != 0:
            first = self._first._data
            self._first = self._first._next
            self._size -= 1
            return first

    def clear(self): # Time complexity O(1), since it only reassigns values
        """"Removes all elements from this list"""
        if self._size != None:
            self._first = None
            self._last = None
            self._size = 0

    def size(self): # Time complexity O(1), only accesses and returns a single value
        """Returns the number of elements in this list"""
        return self._size

    def string(self): # Time complexity O(n), since it has to go through all elements in the list
        """Returns a string representation of this list"""
        if self._first == None:
            return "The list is empty."
        else:
            string = ""
            index = self._first
            while index != None: # Converts elements to string and adds them to empty string
                string += str(index._data) + ", "
                index = index._next
            string = "[" + string[:-2] + "]"
            return string
    
    def healthy(self): # Time complexity O(n), since it has to go through all elements in the list
        """Method that checks if list is working correctly"""
        if self._size == 0:
            assert self._first == None 
            assert self._last == None
        else:
            assert self._last._next == None
            assert self._first != None
            assert self._last != None
            counter = 0
            index = self._first
            while index != None: # Counts number of elements in list and compares with list size
                counter += 1
                index = index._next
            assert self._size == counter


# Unit test
def main():
    list = LinkedList()
    list.healthy()
    assert list.getFirst() == None
    list.addFirst(2)
    list.addLast(4)
    list.addLast(8)
    list.addLast("hej")
    list.healthy()
    assert list.get(-3) == None
    assert list.get(0) == 2
    assert list.string() == "[2, 4, 8, hej]"
    list.healthy()
    assert list.getFirst() == 2
    assert list.size() == 4
    assert list.getLast() == "hej"
    list.removeFirst()
    list.removeFirst()
    list.removeFirst()
    list.healthy()
    list.removeFirst()
    assert list.size() == 0
    list.healthy()
    list.addFirst(63)
    assert list.getFirst() == 63
    list.healthy()
    assert list.size() == 1
    list.addLast(16)
    assert list.get(5) == None
    assert list.get(1) == 16
    list.addFirst([1, 2])
    assert list.size() == 3
    list.healthy()
    list.clear()
    assert list.removeFirst() == None
    assert list.size() == 0
    list.healthy()
    assert list.string() == "The list is empty."


main()


if __name__ == "__main__":
    main()
