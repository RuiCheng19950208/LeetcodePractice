class Solution(object):
    def findMaxConsecutiveOnes(self, nums):
        ans=0
        count=0

        for i in nums:
            if i==1:
                count=count+1
            else: count=0
            if count>ans:
                ans=count


        return ans



print(Solution().findMaxConsecutiveOnes([1,1,1,0,1,1]))