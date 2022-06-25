from unittest import skip


def search(nums, target):
    n = len(nums)
    lowerBound = 1
    upperBound = n

    while True:
        if upperBound < lowerBound:
            return -1
        midPoint = int(lowerBound + (upperBound - lowerBound) / 2)
        if nums[midPoint] < target:
            lowerBound = midPoint + 1
        elif nums[midPoint] > target:
            upperBound = midPoint - 1
        elif nums[midPoint] == target:
            return midPoint
    

print(search(nums = [-1,0,3,5,9,12], target = 2))