def trimMean(arr):
    arr.sort()
    toRem = int((len(arr) / 100) * 5)
    arr = arr[toRem:-toRem]
    return sum(arr) / len(arr)

print(trimMean([6,0,7,0,7,5,7,8,3,4,0,7,8,1,6,8,1,1,2,4,8,1,9,5,4,3,8,5,10,8,6,6,1,0,6,10,8,2,3,4]))