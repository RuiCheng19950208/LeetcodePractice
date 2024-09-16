class Solution(object):
    def setZeroes(self, matrix):
        hang=[]
        lie=[]
        for i in range(0,len(matrix)):
            for j in range(0,len(matrix[0])):
                if matrix[i][j]==0:
                    hang.append(i)
                    lie.append(j)
        for i in range(0,len(matrix)):
            for j in range(0,len(matrix[0])):
                if i in hang or j in lie:
                    matrix[i][j]=0




        return matrix


print(Solution().setZeroes([
  [1,1,1],
  [1,0,1],
  [1,1,1],
  [1,1,1]
]))