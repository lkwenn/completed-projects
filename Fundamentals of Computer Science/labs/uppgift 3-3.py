# Linnea Wennberg, grudat24 uppg 3.3

def partition(v): # Time complexity O(n), in-place algorithm
    """Sorts and returns a list with all the negative numbers first"""
    low, mid, high = 0, 0, len(v)
    try: 
        while mid < high:
            """ Invariant:
            - v[:low] < 0
            - v[low:mid] = 0
            - v[mid:high] are unknown
            - v[high] > 0
                    < 0       = 0        unknown       > 0
                -----------------------------------------------
            v: |          |          |a            |           |
                -----------------------------------------------
                            ^          ^             ^
                        low        mid           high
            
            Source: yourbasic.org/golang/quicksort-optimizations/
            """
            a = v[mid]
            if a < 0:
                v[mid] = v[low]
                v[low] = a
                low +=1
                mid +=1
            elif a == 0:
                mid +=1
            else: # if a > p
                v[mid] = v[high-1]
                v[high-1] = a
                high -= 1
        return v
    except TypeError:
        return "List can only contain integers and floats"


v01 = []
v02 = [0]
v2 = [1, 3, -3, -16, 2, 6, 9, -1, 0, 0, -24]
v3 = [53,  24, 3, 1, 1, 7, 7, 8, 1]
v4 = [3.4, 5.6, 1, -5.5, -50, 3.3, -2]
v5 = ["hej", 3]


#Unit test
assert partition(v01) == []
assert partition(v02) == [0]

assert partition(v2) == [-24, -3, -16, -1, 0, 0, 9, 6, 2, 3, 1]
assert partition(v3) == [24, 3, 1, 1, 7, 7, 8, 1, 53]
assert partition(v4) == [-2, -50, -5.5, 1, 3.3, 5.6, 3.4]

assert partition(v5) == "List can only contain integers and floats"