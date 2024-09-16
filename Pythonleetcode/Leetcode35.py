def searchInsert( nums, target):
    if len(nums) == 1:
        if target <= nums[0]:
            return 0
        else:
            return 1

    for i in range(0, len(nums) - 1):
        if target < nums[0]:
            return 0
            break
        if nums[i] == target:
            return i
            break
        if nums[i] < target and nums[i + 1] >= target:
            return i + 1
            break
    return len(nums)



nums=[1]
print(nums[0])
print(searchInsert(nums,0))
