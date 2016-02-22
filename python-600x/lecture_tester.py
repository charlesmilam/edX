def swapSort(L):
    """ L is a list on integers """
    print "Original L: ", L
    for i in range(len(L)):
        for j in range(len(L)):
            if L[j] < L[i]:
                # the next line is a short
                # form for swap L[i] and L[j]
                L[j], L[i] = L[i], L[j]
                print L
    print "Final L: ", L

nums = [1, 5, 0, 15, 3, 7, 21, 2]
nums1 = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
nums2 = [9, 8, 7, 6, 5, 4, 3, 2, 1, 0]

swapSort(nums)
swapSort(nums1)
swapSort(nums2)
