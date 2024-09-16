class Solution(object):
    def coinChange(self, coins, amount):

        dp=[-1]*(1+amount)
        dp[0]=0
        for i in range(1, amount+1):
            for j in range(len(coins)):
                if i>=coins[j] and dp[i-coins[j]]!=-1 :
                    if dp[i]>dp[i-coins[j]]+1 or dp[i]==-1:
                        dp[i]=dp[i-coins[j]]+1
        return dp[-1]




print(Solution().coinChange([ 2, 5], 12))