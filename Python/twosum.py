

# Contains2sum

def Contains2Sum(L, target):
    newL=[]
    if(L):
        for i in range(0, L):
            for j in range(1, L):
                if L[i] + L[j] == target:
                    newL.append(True)
    else:
        return false
