#!/usr/bin/python3

def add(a, b):
    """
    Add two numbers

    Example:
    >>> add(2, 3) # doctest: +ELLIPSIS
    ...
    >>> add(5, -5) #doctest: +NORMALIZE_WHITESPACE 
    0

    >>> add('a', 'b') # doctest: +IGNORE_EXCEPTION_DETAIL
    traceback (most recent call last)
        ...
    TypeError: unsupported operand type(s) for +: 'str' and 'str'
    """
    return a + b


if __name__ == "__main__":
    print(add(6,-    6))
