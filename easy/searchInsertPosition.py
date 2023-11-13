def searchInsert(nums, target):
    for index, val in enumerate(nums):
        if val >= target:
            return index
    return len(nums)


print(searchInsert([1, 2, 7, 8], 50))
