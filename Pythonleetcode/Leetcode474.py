class Solution(object):
    def findMaxForm(self, strs, m, n):
        dp=[]
        for k in range(len(strs)+1):
            temp=[]
            for i in range(m+1):
                temp.append([0]*(n+1))
            dp.append(temp)
        # print(len(dp),len(strs)+1)
        # print(len(dp[0]), m + 1)
        # print(len(dp[0][0]), n + 1)
        for k in range(1,len(strs)+1):
            zeros=strs[k-1].count('0')
            ones=strs[k-1].count('1')
            for i in range(m+1):
                for j in range(n+1):
                    if j>=ones and i>=zeros:
                        dp[k][i][j]=max([dp[k-1][i][j],dp[k-1][i-zeros][j-ones]+1])
                    else:
                        dp[k][i][j] = dp[k - 1][i][j]

        # print(dp)
        return dp[-1][-1][-1]

print(Solution().findMaxForm( strs = ["10","0001","111001","1","0"], m = 5, n = 3))
print(Solution().findMaxForm(strs = ["10","0","1"], m = 1, n = 1))