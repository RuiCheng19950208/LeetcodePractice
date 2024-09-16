class Solution(object):
    def transpose(self, A):

        n=len(A)
        m=len(A[0])
        result=[[0 for i in range(n)]for j in range(m)]


        for j in range(n):
            for i in range(m):
                result[i][j]=A[j][i]

        return result




print(Solution().transpose( [[1,2],[4,5],[7,8]]))