class Solution(object):
    def isToeplitzMatrix(self, matrix):
        A=len(matrix)
        B=len(matrix[0])
        if A==1 or B==1:
            return True
        for i in range(0,A-1):
            for j in range(0,min( B - 1,A - 1)):
                if matrix[i][j]!=matrix[i+1][j+1]:
                    return False

        for j in range(1,B-1):
            for i in range(0, min(B - 1,A-1)):
                if matrix[i][j]!=matrix[i+1][j+1]:
                    return False

        return True




print(Solution().isToeplitzMatrix([
  [1,2,3,4],
  [5,1,2,3],
  [9,5,1,2]
]))