class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        for i in nums:
            if i == target:
                return nums.index(target)

        else:
            return -1





print(Solution().search(nums = [4,5,6,7,0,1,2], target = 0))
print(Solution().search(nums = [4,5,6,7,0,1,2], target = 3))
print(Solution().search(nums = [1], target = 0))