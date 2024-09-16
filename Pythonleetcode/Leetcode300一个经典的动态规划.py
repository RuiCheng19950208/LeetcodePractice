class Solution(object):
    def lengthOfLIS(self, nums):
        l=len(nums)
        ans=[1]*(l)
        if nums==[]:
            return 0

        for i in range(1,l):
            for j in range(i):
                if nums[i]>nums[j]:
                    ans[i]=max(ans[j]+1,ans[i])
        return max(ans)





print(Solution().lengthOfLIS([10,9,2,5,3,7,101,18]))
print(Solution().lengthOfLIS([1,3,6,7,9,4,10,5,6]))
