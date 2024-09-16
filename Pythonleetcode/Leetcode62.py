class Solution(object):
    def uniquePaths(self, m, n):

        def jiecheng(k):
            n=1
            for i in range(1,k+1):
                n=n*i

            return n

        return int(jiecheng(m+n-2)/(jiecheng(m-1)*jiecheng(n-1)))





print(Solution().uniquePaths(3,7))
