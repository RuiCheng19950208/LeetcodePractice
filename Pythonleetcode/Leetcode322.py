class Solution(object):
    def coinChange(self, coins, amount):
        dp=[0]*(amount+1)
        for i in range(1,amount+1):
            temp=[dp[i-k]+1 for k in coins if k<=i and dp[i-k]!=-1]
            if len(temp)>0:
                dp[i]=min(temp)
            else:
                dp[i]=-1
        # print(dp)
        return dp[-1]

print(Solution().coinChange(coins = [1,2,5], amount = 11))
print(Solution().coinChange(coins = [2], amount = 3))
print(Solution().coinChange(coins = [1], amount = 0))
print(Solution().coinChange(coins = [1], amount = 1))