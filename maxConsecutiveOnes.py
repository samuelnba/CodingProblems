def findMaxConsecutiveOnes(nums):
    b = 0
    c = 0
    for i in nums:
        if i == 1:
            c += 1
        else:
            if b < c:
                b = c
            c = 0
    if b < c:
        b = c
    return b

print(findMaxConsecutiveOnes([1,1,0,1,1,1]))