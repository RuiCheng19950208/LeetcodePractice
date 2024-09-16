class Solution(object):
    def canPartition(self, nums):
        T=sum(nums)
        if T%2==0:
            T=int(T/2)
        else:
            return False

        dp=[]
        for i in range(len(nums)+1):
            dp.append([1]+[0]*T)

        for i in range(1,len(nums)+1):
            for j in range(1,T+1):
                if j-nums[i-1]>=0:
                    dp[i][j]=dp[i-1][j]+dp[i-1][j-nums[i-1]]
                else:
                    dp[i][j] = dp[i - 1][j]

        # print(dp)
        return dp[-1][-1]>0

print(Solution().canPartition([1,5,11,5]))
print(Solution().canPartition([1,2,3,5]))