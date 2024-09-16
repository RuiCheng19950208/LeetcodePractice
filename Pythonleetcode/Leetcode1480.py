class Solution(object):
    def runningSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        ans=[0]*len(nums)
        ans[0]=nums[0]
        for i in range(1,len(nums)):
            ans[i] = ans[i-1]+nums[i]

        return ans


print(Solution().runningSum([1,2,3,4]))
print(Solution().runningSum( [1,1,1,1,1]))
print(Solution().runningSum([3,1,2,10,1]))
