def balanced(expression):
    """
    >>> balanced("(x+y)*(z-2*(6))")
    True
    >>> balanced("7-(3(2*9))4)(")
    False
    >>> balanced("ak")
    True
    """
    #your code goes here
    lst  = []
    if all(s not in expression for s in [")", "(", "[", "]", "{", "}"]):
        return True
    for a in expression:
        if a == "(":
           lst.insert(0,a)
        if a == ")":
           if len(lst)==0:
               return False
           if lst[0]=="(":
               lst.pop(0)
           else:
              return False
    for a in expression:
        if a == "[":
           lst.insert(0,a)
        if a == "]":
           if lst[0]=="[":
               lst.pop(0)
           else:
              return False
    for a in expression:
        if a == "{":
           lst.insert(0,a)
        if a == "}":
           if lst[0]=="{":
               lst.pop(0)
           else:
              return False
    return not bool(len(lst))

if __name__ == '__main__':
    import doctest
    print(doctest.testmod())