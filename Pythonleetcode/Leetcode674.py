class Solution(object):
    def findLengthOfLCIS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        ans=1
        tem_ans = 1
        if len(nums)==0:
            return 0
        for i in range(1,len(nums)):
            if nums[i]>nums[i-1]:
                tem_ans +=1
                if tem_ans>ans:
                    ans=tem_ans
            else:
                tem_ans = 1
        return ans





print(Solution().findLengthOfLCIS([1,3,5,4,7]))
print(Solution().findLengthOfLCIS([2,2,2,2,2]))