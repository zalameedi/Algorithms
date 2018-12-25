# Implementation of the shell sort algorithm

def shellSort(L):
    myL = []
    increment = len(L)//2
    while increment > 0:
        for i in range(increment):
            myL = insertionSort(L, i, increment)
            increment = increment // 2
    return myL


# Edited to take start, mid, end
def insertionSort(L, start, gap):
    if gap != 0:
        for i in range(start+gap, len(L), gap): #Go up by the gap value # Incre != 0
            cur = L[i]
            pos = i

            while pos >= gap and L[pos-gap]>cur:
                L[pos]=L[pos-gap]
                pos=pos-gap

            L[pos] = cur 
    else:
        return L 

def main():
    L = [101, 77, 68, 26, 11, 7, 1337, 70, 16, 21]
    print(shellSort(L))

main()
