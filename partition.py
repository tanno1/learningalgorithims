#Noah Tanner
#Chapter 1 Challenge Problems
#December 2022

#Partition Example

import random

def partition(A, lo, hi, idx):
    if lo == hi: return lo

    A[idx],A[lo] = A[lo],A[idx] #swap
    i = lo
    j = hi + 1

    while True:
        while True:
            i += 1
            if i == hi: break
            if A[lo] < A[i]: break
        
        while True:
            j -= 1
            if j == lo: break
            if A[j] < A[lo]: break

        if i >= j: break
        A[i],A[j] = A[j],A[i]

    A[lo],A[j] = A[j],A[lo]
    return j

def linear_median(A):
    lo = 0
    hi = len(A) - 1
    mid = hi //2 
    while lo < hi:
        idx = random.randint(lo, hi) #select random index
        j = partition(A, lo, hi, idx)

        if j == mid:
            return A[j]
        if j < mid:
            lo = j+1
        else: 
            hi = j-1
    return A[lo]

A = [1, 3, 5, 2, 4, 6, 9, 7, 8]

linear_median(A)

print(A)