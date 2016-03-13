def getSublists(L, n):
    sublists = []
    start_idx = 0

    while len(L[start_idx:start_idx + n]) == n:
        sublists.append(L[start_idx:start_idx + n])
        start_idx += 1

    return sublists

def longestRun(L):
    best_run = 1
    sub_len = 1
    good_run = None

    while sub_len <= len(L):
        for lst in getSublists(L, sub_len):
            for idx, el in enumerate(lst):
                if idx > 0:
                    if lst[idx] >= lst[idx - 1]:
                        good_run = True
                    else:
                        good_run = False
                        break

            if good_run:
                best_run = len(lst)

            good_run = None

        sub_len += 1

    return best_run

# Test
L = [10, 4, 6, 8, 3, 4, 5, 7, 7, 2]
print 'Expected: 5'
print 'Actual:', longestRun(L)
