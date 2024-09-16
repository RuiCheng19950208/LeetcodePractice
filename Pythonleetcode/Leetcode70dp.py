class Solution(object):
    def climbStairs(self, n):
        dp=[0]*(n+1)
        dp[1]=1
        dp[0]=1
        if n<=1:
            return  dp[n]
        else:
            for i in range(2,n+1):
                dp[i]=dp[i-2]+dp[i-1]

        return dp[n]

print(Solution().climbStairs(2))
print(Solution().climbStairs(3))


