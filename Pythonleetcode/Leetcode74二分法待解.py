class Solution(object):
    def searchMatrix(self, matrix, target):
      leftline=0
      rightline=len(matrix)-1
      left=0
      right=len(matrix[0])-1
      while leftline!=rightline :
        if matrix[leftline][-1]<target:
          leftline=(leftline+rightline)//2+1
        else:leftline=leftline//2
        if matrix[rightline][0]>target:
          rightline=(leftline+rightline)//2
        else:rightline = (rightline+len(matrix)) // 2



        if leftline==rightline:
          while left!=right:
            if (matrix[leftline][right] == target or matrix[leftline][left] == target):
              return True

            if matrix[leftline][right] < target:
              left = (left + right) // 2
            else:left=left//2


            if matrix[rightline][left] > target:
              right = (left + right) // 2
            else:right = (right+len(matrix[0])) // 2
            print(leftline, rightline, left, right)






      return False














print(Solution().searchMatrix([
  [1,   3,  5,  7],
  [10, 11, 16, 20],
  [23, 30, 34, 50]
],3))


print(Solution().searchMatrix( [
  [1,   3,  5,  7],
  [10, 11, 16, 20],
  [23, 30, 34, 50]
],13))