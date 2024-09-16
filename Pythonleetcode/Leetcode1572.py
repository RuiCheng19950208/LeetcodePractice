class Solution(object):
    def diagonalSum(self, mat):
        """
        :type mat: List[List[int]]
        :rtype: int
        """
        ans=0

        if len(mat)%2==0:
            for i in range(len(mat)):
                for j in range(len(mat[0])):
                    if i==j:
                        ans +=mat[i][j]
                    if i+j==len(mat)-1:
                        ans +=mat[i][j]

            return ans
        else:
            for i in range(len(mat)):
                for j in range(len(mat[0])):
                    if i == j:
                        ans += mat[i][j]
                    if i + j == len(mat) - 1:
                        ans += mat[i][j]
            ans -= mat[len(mat)//2][len(mat)//2]

            return ans




print(Solution().diagonalSum(mat = [[1,1,1,1],
              [1,1,1,1],
              [1,1,1,1],
              [1,1,1,1]]))


print(Solution().diagonalSum(mat = [[5]]))