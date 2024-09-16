class Solution(object):
    def searchMatrix(self, matrix, target):
        if  target>matrix[-1][-1] or target<matrix[0][0]:
            return False
        low_row=0
        high_row=len(matrix)-1
        while low_row<high_row:
            target_row = (low_row + high_row) // 2
            if  target>=matrix[target_row][0] and target<=matrix[target_row][-1]:
                low_row=target_row
                high_row=target_row
            elif target<matrix[target_row][0]:
                high_row=target_row-1
            elif target>matrix[target_row][-1]:
                low_row=target_row+1
            # print(low_row,high_row)

        for i in matrix[low_row]:
            if i==target:
                return True
            elif i>target:
                return False

        return False


print(Solution().searchMatrix(matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]], target = 3))
print(Solution().searchMatrix(matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]], target = 13))

