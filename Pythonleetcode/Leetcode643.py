import copy
class Solution(object):
    def findMaxAverage(self, nums, k):
        ans=0
        for i in range(0,k):
            ans=ans+nums[i]
        m=copy.deepcopy(ans)
        for i in range(0,len(nums)-k):
            if ans-nums[i]+nums[i+k]>m:
                m=ans-nums[i]+nums[i+k]
                ans=ans-nums[i]+nums[i+k]
            else:ans=ans-nums[i]+nums[i+k]
        return float(m)/float(k)






print(Solution().findMaxAverage([1,12,-5,-6,50,3], 4))