class Solution(object):
    def search(self, nums, target):
        for i in range(len(nums)):
            if nums[i]==target:
                return i
        return -1



print(Solution().search([-1,0,3,5,9,12],  1))