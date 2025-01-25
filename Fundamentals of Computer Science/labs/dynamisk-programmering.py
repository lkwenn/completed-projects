# Linnea Wennberg, grudat24 uppg 5.1

def knitting(n: int, h: list) -> int:
    if not isinstance(n, int):
        raise TypeError("Input must be an integer")
    p = 0
    if n == 0:
        return 0
    elif n > 0:
        if n > 4:
            h.extend([0]*(n-4))
        for i in range(1, n+1):
            p = max(p, h[i] + knitting(n-i, h))
        return p
    else:
        raise ValueError("Integer must be non-negative")


def cached(n: int, h: list, profit = {}) -> int:
    if not isinstance(n, int):
        raise TypeError("Input must be an integer")
    p = 0
    if n in profit:
        return profit[n]
    if n == 0:
        return 0
    elif n > 0:
        if n > 4:
            h.extend([0]*(n-4))
        for i in range(1, n+1):
            p = max(p, h[i] + cached(n-i, h))
        profit[n] = p
        return p
    else:
        raise ValueError("Integer must be non-negative")


def main():
    h = [0, 2, 5, 6, 9]
    # Testing standard inputs
    assert knitting(0, h) == 0
    assert knitting(1, h) == 2
    assert knitting(5, h) == 12

    assert cached(0, h) == 0
    assert cached(1, h) == 2
    assert cached(5, h) == 12

    # Testing incorrect inputs
    func = [knitting, cached]
    for f in func:
        incorrect_types = [4.3, "hej", [], (1, 2)]
        for type in incorrect_types:
            try:
                f(input, h)
                raise AssertionError("{} should have resulted in TypeError".format(type))
            except TypeError:
                pass
    
        # Testing negative values
        neg_values = [-2, -5]
        for value in neg_values:
            try:
                f(value, h)
                raise AssertionError("{} should have resulted in ValueError".format(value))
            except ValueError:
                pass


main()