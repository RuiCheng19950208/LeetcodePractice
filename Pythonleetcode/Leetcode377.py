class Solution(object):
    def combinationSum4(self, nums, target):
        dp=[1]+[0]*target
        for i in range(1,target+1):
            dp[i]=sum([dp[i-k] for k in nums if i-k>=0])
        return dp[-1]

print(Solution().combinationSum4(nums = [1, 2, 3],target = 4))