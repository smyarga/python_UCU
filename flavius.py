def sieve_flavius(n):
    """
    sieve_flavius
    >>> sieve_flavius(100)
    [1, 3, 7, 9, 13, 15, 21, 25, 31, 33, 37, 43, 49, 51, 63, 67, 69, 73, 75, 79, 87, 93, 99]
    >>> sieve_flavius(10)
    [1, 3, 7, 9]
    >>> sieve_flavius(0)
    []
    >>> sieve_flavius(9)
    [1, 3, 7, 9]
    """
    lst = [i for i in range(1, n+1, 2)]
    for i in lst:
        if i == 1:
            continue
        del lst[i - 1::i]
    return lst

if __name__ == '__main__':
    import doctest
    print(doctest.testmod())