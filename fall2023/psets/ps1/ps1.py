from asyncio import base_tasks
import math
import time
import random

"""
See below for mergeSort and countSort functions, and for a useful helper function.
In order to run your experiments, you may find the functions random.randint() and time.time() useful.

In general, for each value of n and each universe size 'U' you will want to
    1. Generate a random array of length n whose keys are in 0, ..., U - 1
    2. Run count sort, merge sort, and radix sort ~10 times each,
       averaging the runtimes of each function. 
       (If you are finding that your code is taking too long to run with 10 repitions, you should feel free to decrease that number)

To graph, you can use a library like matplotlib or simply put your data in a Google/Excel sheet.
A great resource for all your (current and future) graphing needs is the Python Graph Gallery 
"""


def merge(arr1, arr2):
    helperarr = []

    i = 0
    j = 0
    while i < len(arr1) or j < len(arr2):
        if i >= len(arr1):
            helperarr.append(arr2[j])
            j += 1
        elif j >= len(arr2):
            helperarr.append(arr1[i])
            i += 1
        elif arr1[i][0] <= arr2[j][0]:
            helperarr.append(arr1[i])
            i += 1
        else:
            helperarr.append(arr2[j])
            j += 1

    return helperarr

def mergeSort(arr):
    if len(arr) < 2:
        return arr

    midpt = int(math.ceil(len(arr)/2))

    half1 = mergeSort(arr[0:midpt])
    half2 = mergeSort(arr[midpt:])

    return merge(half1, half2)

def countSort(univsize, arr):
    universe = []
    for i in range(univsize):
        universe.append([])

    for elt in arr:
        universe[elt[0]].append(elt)

    helperarr = []
    for lst in universe:
        for elt in lst:
            helperarr.append(elt)

    return helperarr

def BC(n, b, k):
    if b < 2:
        raise ValueError()
    digits = []
    for i in range(k):
        digits.append(n % b)
        n = n // b
    if n > 0:
        raise ValueError()
    return digits

def radixSort(univsize, base, arr):
    """TODO: Implement Radix Sort using BC and countSort"""
    k = math.ceil(math.log(univsize, base))
    helperarr = []
    for i in range(len(arr)):
        helperarr.append([i, [arr[i][1]]])
    for i in range(len(arr)):
        helperarr[i][1].append(BC(arr[i][0], base, k))
    for j in range(k):
        for i in range(len(arr)):
            helperarr[i][0] = helperarr[i][1][1][j]
        helperarr = countSort(base, helperarr)
    finalarr = []
    for i in range(len(arr)):
        ki = 0
        for j in range(k):
            ki += helperarr[i][1][1][j] * base**j
        finalarr.append([ki, helperarr[i][1][0]])
    
    return finalarr

testarr = [[10, "A"], [5, "B"], [100, "C"], [3, "D"], [16, "E"]]
print(radixSort(101, 10, testarr))
