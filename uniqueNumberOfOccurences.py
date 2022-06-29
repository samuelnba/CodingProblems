def uniqueOccurences(arr):
    occurences = []
    arr2 = list(dict.fromkeys(arr))
    for i in arr2:
        temp = 0
        for j in arr:
            if i == j:
                temp += 1
        occurences.append(temp)
    for i in range(len(occurences)):
        for j in range(len(occurences)):
            if occurences[i] == occurences[j] and j != i:
                return False
    return True

print(uniqueOccurences([1,2,2,1,1,3]))