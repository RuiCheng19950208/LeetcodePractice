class Solution(object):
    def tallestBillboard(self, rods):
        up_limit=sum(rods)
        dp=[[-1]*(up_limit+1) for _ in range(len(rods)+1)]
        dp[0][0]=0
        for i in range(1,len(rods)+1):
            h=rods[i-1]
            for j in range(up_limit+1-h):
                if dp[i-1][j]<0:
                    continue
                dp[i][j]=max(dp[i][j],dp[i-1][j])
                dp[i][j+h]=max(dp[i][j+h],dp[i-1][j])
                dp[i][abs(h-j)]=max(dp[i][abs(h-j)],dp[i-1][j]+min(j,h))
        # print(dp)
        return dp[-1][0]


print(Solution().tallestBillboard([1,2]))
print(Solution().tallestBillboard([1,2,3,6]))
print(Solution().tallestBillboard([1,2,3,4,5,6]))