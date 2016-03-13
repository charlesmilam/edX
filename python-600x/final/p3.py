def dict_invert(d):
    '''
    d: dict
    Returns an inverted dictionary. The inverse of a dictionary d is another dictionary whose keys are the unique dictionary values in d. The value for a key in the inverse dictionary is a sorted list of all keys in d that have the same value in d.
    '''
    inverted_dict = {}

    for item in d:
        try:
            item_list = inverted_dict[d[item]]
            item_list.append(item)
            inverted_dict[d[item]] = item_list
        except:
            inverted_dict[d[item]] = [item]

    return inverted_dict

 # Test 1
print 'Expected: {10: [1], 20: [2], 30: [3]}'
print 'Actual:', dict_invert({1:10, 2:20, 3:30})

# Test 2
print 'Expected: {10: [1], 20: [2], 30: [3, 4]}'
print 'Actual:', dict_invert({1:10, 2:20, 3:30, 4:30})

# Test 3
print 'Expected: {True: [0, 2, 4]}'
print 'Actual:', dict_invert({4:True, 2:True, 0:True})
