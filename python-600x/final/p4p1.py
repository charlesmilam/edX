def getSublists(L, n):
    sublists = []
    start_idx = 0

    while len(L[start_idx:start_idx + n]) == n:
        sublists.append(L[start_idx:start_idx + n])
        start_idx += 1

    return sublists

# Test 1
L = [10, 4, 6, 8, 3, 4, 5, 7, 7, 2]
n = 4
print 'Expected: [[10, 4, 6, 8], [4, 6, 8, 3], [6, 8, 3, 4], [8, 3, 4, 5], [3, 4, 5, 7], [4, 5, 7, 7], [5, 7, 7, 2]]'
print 'Actual:', getSublists(L, n)

# Test 2
L = [1, 1, 1, 1, 4]
n = 2
print 'Expected: [[1, 1], [1, 1], [1, 1], [1, 4]]'
print 'Actual:', getSublists(L, n)
