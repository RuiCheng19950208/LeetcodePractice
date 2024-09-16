class Solution(object):
    def change(self, amount, coins):
        coins.sort()
        dp=[]
        if amount==0:
            return 1
        elif len(coins)==0 and amount>0:
            return 0
        for i in range(len(coins)+1):
            temp=[1]+[0]*amount
            dp.append(temp)
        if len(coins)==1:
            for j in range(1,amount+1):
                if j%coins[0]==0:
                    dp[1][j]=1
            return dp[-1][-1]
        else:
            for j in range(1,amount+1):
                if j%coins[0]==0:
                    dp[1][j]=1
            for i in range(2,len(coins)+1):
                for j in range(1,amount+1):
                    if j-coins[i-1]<0:
                        dp[i][j] = dp[i-1][j]
                    else:
                        dp[i][j] = dp[i-1][j]+dp[i][j-coins[i-1]]
            return dp[-1][-1]


print(Solution().change(amount = 5, coins = [1, 2, 5]))
print(Solution().change(amount = 3, coins = [2]))
print(Solution().change(amount = 10, coins = [10] ))