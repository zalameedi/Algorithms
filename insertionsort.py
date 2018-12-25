# Implementation of the insertion sort algorithm

def insertionSort(L):
    for i in range(1, len(L)):
        cur = L[i]
        pos = i

        while pos > 0 and L[pos-1]>cur:
            L[pos]=L[pos-1]
            pos=pos-1

        L[pos] = cur 
    return L 

def main():
    L = [101, 77, 68, 26, 11, 7, 1337, 70, 16, 21]
    print(insertionSort(L))

main()
