def removeElement(nums, val):
    nums2=nums[:]
    for i in range(0,len(nums)):
        if nums2[i]==val:
            nums.remove(val)

    return len(nums)
print(removeElement([2,2,3,3,2],2))
