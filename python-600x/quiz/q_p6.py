def flatten(aList):
    '''
    aList: a list
    Returns a copy of aList, which is a flattened version of aList
    '''
    return_list = []

    for item in aList:
        if type(item) == list:
            for list_item in flatten(item):
                # print 'list item', list_item
                return_list.append(list_item)
        else:
            return_list.append(item)

    return return_list


print flatten([[1], [1]])
