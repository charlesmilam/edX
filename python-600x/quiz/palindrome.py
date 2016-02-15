def isPalindrome(aString):
    '''
    aString: a string
    '''
    if len(aString) <= 1:
        return False

    rev_str = ''

    for char in aString:
        rev_str = char + rev_str

    print 'strs', aString, rev_str

    return aString == rev_str

print 'Should return False: ' + str(isPalindrome(''))
print 'Shoule return False: ' + str(isPalindrome('a'))
