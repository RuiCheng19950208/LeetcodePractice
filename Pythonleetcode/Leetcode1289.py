class Solution(object):
    def minFallingPathSum(self, arr):
        col=len(arr[0])
        row = len(arr)
        dp=[]
        for i in range(row):
            dp.append([0]*col)

        for i in range(row):
            for j in range(col):
                if i==0:
                    dp[0][j]=arr[0][j]
                else:
                    dp[i][j]=arr[i][j]+min(dp[i-1][k] for k in range(col) if k!=j)
                # print(dp)
        return min(dp[row-1][k] for k in range(col))






print(Solution().minFallingPathSum([[1,2,3],[4,5,6],[7,8,9]]))