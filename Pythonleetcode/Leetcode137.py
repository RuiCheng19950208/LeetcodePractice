class Solution(object):
    def singleNumber(self, nums):
        nums.sort()
        if len(nums) == 1:
            return nums[0]
        if nums[0] != nums[1]:
            return nums[0]
        if nums[len(nums) - 1] != nums[len(nums) - 2]:
            return nums[len(nums) - 1]

        for i in range(3, len(nums) - 3):
            if nums[i] != nums[i - 1] and nums[i] != nums[i + 1]:
                return nums[i]





print(Solution().singleNumber([2,2,3,2]))
print(Solution().singleNumber([0,1,0,1,0,1,99]))