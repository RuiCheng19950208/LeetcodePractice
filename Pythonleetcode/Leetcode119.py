class Solution(object):
    def getRow(self, rowIndex):
        def jiecheng(n):
            if n==0:
                return 1
            k=1
            for i in range(1,n+1):
                k=i*k
            return k


        ans=[1]*(rowIndex+1)

        for i in range(0, rowIndex):

            ans[i]=int(jiecheng(rowIndex)/(jiecheng(rowIndex-i)*jiecheng(i)))
        return ans

print(Solution().getRow(5))

