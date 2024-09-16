class Solution(object):
    def numSquares(self, n):
        ans=[n]*(n+1)
        ans[0] = 0
        ans[1]=1
        for i in range(2,n+1):
            j=1
            while(j*j<=i):
                ans[i] = min(ans[i], ans[i - j * j] + 1)

                j = j + 1

        return ans[n]





print(Solution().numSquares(13))