# Bubble sort implementation

def bubbleSort(L):
    i=0
    for i in range (0, len(L)):
        for j in range (0, len(L)):
            try: 
                if L[j] > L[j+1]:
                    temp = L[j]
                    L[j] = L[j+1]
                    L[j+1] = temp
                    cont = False 
            except:
                pass
    return L

        
def main():
    L = [101, 77, 68, 26, 11, 7, 1337, 70, 16, 21]
    print(bubbleSort(L))

if __name__ == '__main__':
    main()