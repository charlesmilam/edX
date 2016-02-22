def f(s):
    return 'a' in s

L = ['a', 'b']

def satisfiesF(L):
    """
    Assumes L is a list of strings
    Assume function f is already defined for you and it maps a string to a Boolean
    Mutates L such that it contains all of the strings, s, originally in L such
            that f(s) returns True, and no other elements. Remaining elements in L
            should be in the same order.
    Returns the length of L after mutation
    """
    working = []

    for idx in range(len(L)):
        if f(L[idx]):
            working.append(L[idx])

    L = working
    print L
    return len(L)

print satisfiesF(L)
