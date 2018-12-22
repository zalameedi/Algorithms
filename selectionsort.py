# Selection sort implementation

def selectionSort(L):
    for i in range(0, len(L)):
        pos = i 
        for j in range(0, len(L)):
            if L[pos] < L[j]:
                pos = j 
                L[i], L[pos] = L[pos], L[i]
    return L


def main():
    L = [101, 77, 68, 26, 11, 7, 1337, 70, 16, 21]
    print(selectionSort(L))

if __name__ == '__main__':
    main()         