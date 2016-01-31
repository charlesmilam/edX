def oddTuples(aTup):
    '''
    aTup: a tuple

    returns: tuple, every other element of aTup.
    '''
    # Your Code Here
    result = ()
    i = 1
    for el in aTup:
        if  i % 2 != 0:
            result += (el, )
        i += 1

    return result

# slick version, provided by prof
def oddTuples2(aTup):
    '''
    Another way to solve the problem.

    aTup: a tuple

    returns: tuple, every other element of aTup.
    '''
    # Here is another solution to the problem that uses tuple
    #  slicing by 2 to achieve the same result
    return aTup[::2]
