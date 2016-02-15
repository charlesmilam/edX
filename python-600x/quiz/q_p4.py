def dotProduct(listA, listB):
    '''
    listA: a list of numbers
    listB: a list of numbers of the same length as listA
    '''
    total = 0

    for idx in range(len(listA)):
        print listA[idx], listB[idx]
        total += listA[idx] * listB[idx]

    return total

print str(dotProduct([-90, 74, 39, 89, -24, -71, 44, -98], [15, 61, 33, -45, 47, 0, -9, -58]))
