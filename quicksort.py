# Implementation of the Quick sort algorithm
import random


def partition(L, l, h):
    pivot = L[len(L)-1]
    init = -1

    
    for i in range(init, len(L)-1):
        if L[i]<=pivot:
            init+=1
            L[init],L[i] = L[i], L[init]
    L[init+1],L[len(L)-1] = L[len(L)-1], L[init+1]
    return(init+1)


def quickSortHelper(L, l, h):
    pivot = L[h]# Choose pivot (randomly to avoid O(N^2))
    init = (l-1)
    for i in range(l, h):
        if L[i]<=pivot:
            init+=1
            L[init],L[i] = L[i], L[init]
    L[init+1],L[h] = L[h], L[init+1]
    return(init+1)

def quickSort(L, l, h):
    if l < h:
       seperate = quickSortHelper(L, l, h)
       quickSort(L, l, seperate-1)
       quickSort(L, seperate+1, h)
    return L

def main():
    L = [101, 77, 68, 26, 11, 7, 1337, 70, 16, 21]
    print(quickSort(L, 0, len(L)-1))

if __name__ == '__main__':
    main()