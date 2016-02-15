def isPalindrome(aString):
    '''
    aString: a string
    '''
    aString = aString.lower()
    rev_str = ''

    for char in aString:
        rev_str = char + rev_str

    # print 'strs', aString, rev_str

    return aString == rev_str

print 'Should return False: ' + str(isPalindrome(''))
print 'Shoule return False: ' + str(isPalindrome('a'))
print 'Shoule return False: ' + str(isPalindrome('ab'))
print 'Shoule return True: ' + str(isPalindrome('aba'))
print 'Shoule return True: ' + str(isPalindrome('Able was I ere I saw Elba'))
