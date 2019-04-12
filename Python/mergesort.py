# Implementation of the merge sort algorithm

def mergeSort(L):
    if (len(L) > 1):
        mid = len(L)//2
        startHalf = L[:mid]
        lastHalf = L[mid:]

        #recursive step
        mergeSort(startHalf)
        mergeSort(lastHalf)
        i=0
        j=0
        k=0

        while i < len(startHalf) and j < len(lastHalf):
            if startHalf[i] <= lastHalf[j]:
                L[k]=startHalf[i]
                i=i+1
            else:
                L[k]=lastHalf[j]
                j+=1
            k+=1
        while i < len(startHalf):
            L[k]=startHalf[i]
            i+=1
            k+=1
        while j < len(lastHalf):
            L[k] = lastHalf[j]
            j+=1
            k+=1
        return L


def main():
    L = [101, 77, 68, 26, 11, 7, 1337, 70, 16, 21]
    print(mergeSort(L))

main()


