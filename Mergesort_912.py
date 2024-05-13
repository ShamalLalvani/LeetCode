#Leet Code Problem 912. Sort an Array:
#   Given an array of integers nums, sort the array in ascending order and return it.
#   You must solve the problem without using any built-in functions in O(nlog(n)) time complexity,
#   and with the smallest space complexity possible.

#This function sorts an array (in place, to minimize space complexity) via mergesort, via the helper function combine.
#The number of possible splits in half of this array until reaching a size of one is given by n,
#where 2^n = 1 (hence log(n) splits). In each of these splits, two arrays are merged (via the helper function combine), resulting in 0(nlog(n)) time.

import numpy as np


#Input constraints: s <= m <= e
#This function assumes arr[s:m] and arr[m:e] are sorted. It sorts arr[s:e]. Time complexity 0(n).
def combine(arr,s,m,e):

    arr1, arr2 = arr[s:m+1], arr[m+1:e+1] #copy arrays
    c1,c2 = 0,0 #counters

    i = s

    while c1 < m-s and c2 < e - m:
        if arr1[c1] <= arr2[c2]:
            arr[i] = arr1[c1]
            c1 += 1
        else:
            arr[i] = arr2[c2]
            c2 += 1

        i = i + 1

    if c1 < m-s:
        while c1 < m-s:
            arr[i] = arr1[c1]
            c1 += 1
            i += 1

    if c2 < e - m:
        while c2 < e - m:
            arr[i] = arr2[c2]
            c2 += 1
            i += 1


def mergesort(arr,s,e):

    if s >= e:
        return

    midPoint = (s + e)//2

    mergesort(arr,s,midPoint)
    mergesort(arr,midPoint+1,e)

    combine(arr,s,midPoint,e)


arr = [np.random.random()+i%2 + i%3 for i in range(0,20)]
print('Unsorted array before mergesort: ', str(arr))
mergesort(arr,0,len(arr)-1)
print('Sorted array after mergesort: ', str(arr))

