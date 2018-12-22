#Binary search implementation
import sys
import os

main_L = []
i=0
for i in range(0,1000):
    main_L.append(i)

def binarySearch(L, x):
    first = 0
    last = len(L)-1
    found = False
    
    # remember to init new first/last - 1 to accomodate loops condition
    # eventually
    while first <= (last):
        mid = (first+last)//2
        if L[mid] == x:
            found = True
            return found 
        else:
            if L[mid] > x:
                last = mid-1
            elif L[mid] < x:
                first = mid+1
            else:
                first = last
    return found


def main():
    global main_L
    x = binarySearch(main_L, 21)
    y = binarySearch(main_L, 112)
    z = binarySearch(main_L, 708)
    q = binarySearch(main_L, 1337)
    if x and y and z and not q:
        print("Binary search success.")

if __name__ == '__main__':
    main()

