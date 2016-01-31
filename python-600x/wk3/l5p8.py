def isIn(char, aStr):
    '''
    char: a single character
    aStr: an alphabetized string

    returns: True if char is in aStr; False otherwise
    '''
    # Your code here
    low = 0
    high = len(aStr)
    mid = (low + high) / 2

    if len(aStr) == 0:
        return False
    elif len(aStr) == 1 and char == aStr:
        return True
    elif len(aStr) == 1 and char != aStr:
        return False
    elif aStr[mid] == char:
        return True
    else:
        if char < aStr[mid]:
            aStr = aStr[low:mid]
        else:
            aStr = aStr[mid:high]

        return isIn(char, aStr)
