# Linnea Wennberg, grudat24 uppg 4.2

def counting_sort(v: list, k: int) -> list:
    """Returns a sorted list of integers"""
    if not v or not isinstance(v, list):
        raise TypeError("Input must be a non-empty list")
    else:
        count = [0 for _ in range(k+1)] # Create empty list to store the count of each element
        sorted = [0 for _ in range(len(v))] # Create empty list to store the sorted values

        # Count each element in v
        for i in v:
            if not isinstance(i, int):
                raise TypeError("List can only contain integers")
            elif i >= 0:
                count[i] += 1
            else:
                raise ValueError("List can only contain positive integers")

        # Modify count array by adding the count of the previous element
        for j in range(1, len(count)):
            count[j] += count[j-1]

        # Place the elements in sorted order
        m = len(v)-1
        while m >= 0:
            sorted[count[v[m]]-1] = v[m]
            count[v[m]] -= 1
            m -= 1

        return sorted


def main():
    v0 = [0]
    v1 = [4, 6, 7, 1, 1, 0, 3, 2]
    v2 = [0, 0, 5, 3, 8]
    
    # Testing standard inputs
    assert counting_sort(v0, max(v0)) == [0]
    assert counting_sort(v1, max(v1)) == [0, 1, 1, 2, 3, 4, 6, 7]
    assert counting_sort(v2, max(v2)) == [0, 0, 3, 5, 8]
    
    # Testing incorrect inputs
    incorrect_types = [[], [3.4, 5.6, 1, 5.5], ["hej", 3, 6, 1, "nej"], "hallå", (6, 8)]
    for type in incorrect_types:
        try: 
            counting_sort(type, 0)
            raise AssertionError("{} should have resulted in ValueError".format(type))
        except TypeError:
            pass
    
    # Testing negative values
    try:
        neg = [-2, -3, 1, 4, -8]
        counting_sort(neg, max(neg))
        raise AssertionError("{} should have resulted in ValueError".format(neg))
    except ValueError:
        pass


main()


"""
Denna algoritm har tidskomplexitet O(n+k) och blir linjär om k =< n, k ∈ O(n),
alltså om det högsta värdet i listan är mindre eller lika med antalet element. 
"""
