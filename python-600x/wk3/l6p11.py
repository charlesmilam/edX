def biggest(aDict):
    '''
    aDict: A dictionary, where all the values are lists.

    returns: The key with the largest number of values associated with it
    '''
    # Your Code Here
    if not len(aDict):
        return None
    else:
        max_key = ''
        max_len = 0

        for el in aDict:
            if len(aDict[el]) >= max_len:
                max_len = len(aDict[el])
                max_key = el

        return max_key

# a better way, supplied by prof
def biggest(aDict):
    '''
    aDict: A dictionary, where all the values are lists.

    returns: The key with the largest number of values associated with it
    '''
    result = None
    biggestValue = 0
    for key in aDict.keys():
        if len(aDict[key]) >= biggestValue:
            result = key
            biggestValue = len(aDict[key])
    return result
