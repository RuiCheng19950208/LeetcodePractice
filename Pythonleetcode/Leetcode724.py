class Solution(object):
    def pivotIndex(self, nums):
        he=sum(nums)
        left=0
        for i in range(0,len(nums)):
            if left*2+nums[i]==he:
                return i
            left=left+nums[i]


        return -1





print(Solution().pivotIndex([1, 7, 3, 6, 5, 6]))