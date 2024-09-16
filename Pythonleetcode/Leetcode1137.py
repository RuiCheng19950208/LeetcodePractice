class Solution(object):
    def tribonacci(self, n):
        dp=[0]*(n+1)
        dp[0:3]=[0,1,1]
        if n<3:
            return dp[n]
        else:
            for i in range(3,n+1):
                dp[i]=dp[i-3]+dp[i-2]+dp[i-1]
        return dp[-1]



print(Solution().tribonacci(4))
print(Solution().tribonacci(25))