class Solution(object):
    def arrayPairSum(self, nums):
        nums=sorted(nums)
        ans=0
        for i in range(len(nums)):
            if i%2==0:
                ans=ans+nums[i]
        return ans



print(Solution().arrayPairSum([1,4,3,2]))

