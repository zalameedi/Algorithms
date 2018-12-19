#Sequential search implementation
import sys
import os

main_L = []
i=0
for i in range(0,1000):
    main_L.append(i)


def sequentialSearch(L, x):
    found = False
    index = 0
    ls_size = len(L)
    while (index < ls_size):
        try:
            if(L[index] == x):
                found = True
                return found
            else:
                index += 1
        except:
            sys.excepthook()
    return found

def main():
    global main_L
    x = sequentialSearch(main_L, 21)
    y = sequentialSearch(main_L, 112)
    z = sequentialSearch(main_L, 708)
    q = sequentialSearch(main_L, 1337)
    if x and y and z and not q:
        print("Sequential search success.")

if __name__ == '__main__':
    main()

