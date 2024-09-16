class Solution(object):
    def minFallingPathSum(self, matrix):
        col=len(matrix[0])
        row = len(matrix)
        if col==1:
            return matrix[0][0]
        dp=[]
        for i in range(row):
            dp.append([0]*col)


        for i in range(row):
            for j in range(col):
                if i==0:
                    dp[0][j]=matrix[0][j]*1


                else:
                    if j==0:
                        dp[i][j] = min(dp[i-1][0],dp[i-1][1])+matrix[i][j]
                    elif j==col-1:
                        dp[i][j] =min(dp[i-1][col-1],dp[i-1][col-2])+matrix[i][j]
                    else:
                        dp[i][j]=min(dp[i-1][j-1],dp[i-1][j+1],dp[i-1][j])+matrix[i][j]
                # print(dp)
        return min(dp[row-1][j] for j in range(row))


print(Solution().minFallingPathSum([[2,1,3],[6,5,4],[7,8,9]]))
print(Solution().minFallingPathSum( [[-19,57],[-40,-5]]))
print(Solution().minFallingPathSum([[100,-42,-46,-41],[31,97,10,-10],[-58,-51,82,89],[51,81,69,-51]]))