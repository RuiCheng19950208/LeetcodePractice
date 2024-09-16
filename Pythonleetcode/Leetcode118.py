class Solution(object):
    def generate(self, numRows):
        ans=[[1]]
        if numRows==1:
            return ans
        if numRows == 0:
            return []
        for i in range(1,numRows):
                row=[1]*(i+1)
                ans.append(row)
                for j in range(0, i):
                    if j!=0:
                        ans[i][j]=ans[i-1][j-1]+ans[i-1][j]


        return ans

print(Solution().generate(0))