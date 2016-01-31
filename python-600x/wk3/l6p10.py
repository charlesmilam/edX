def howMany(aDict):
    '''
    aDict: A dictionary, where all the values are lists.

    returns: int, how many values are in the dictionary.
    '''
    # Your Code Here
    accum = 0
    for el in aDict:
        accum += len(aDict[el])

    return accum
