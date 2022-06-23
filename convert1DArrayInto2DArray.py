from calendar import c


def construct2DArray(original, m, n):
    if m * n != len(original):
        return []
    twoD = []
    for i in range(m):
        twoD.append([])
    c = 0
    for i in range(len(twoD)):
        for j in range(n):
            twoD[i].append(original[c])
            c += 1
    return twoD

print(construct2DArray(original = [1,2,3], m = 1, n = 3))
