class Solution(object):
    def numMagicSquaresInside(self, grid):





        ans=0
        def isgrid(matrix):
            if matrix[0][0]+matrix[1][1]+matrix[2][2]!=15 or matrix[0][2]+matrix[1][1]+matrix[2][0]!=15 or sum(matrix[0])!=15 or sum(matrix[1])!=15  or sum(matrix[2])!=15:
                return False
            if matrix[0][0]+matrix[1][0]+matrix[2][0]!=15 or matrix[0][1]+matrix[1][1]+matrix[2][1]!=15 or matrix[0][2]+matrix[1][2]+matrix[2][2]!=15 :
                return False
            if len(list(set(matrix[0]+matrix[1]+matrix[2])))!=9:
                return False
            for i in range(0,3):
                for j in range(0, 3):
                    if matrix[i][j]<1 or matrix[i][j]>9:
                        return False
            return True


        if len(grid)==3 and len(grid[0])>3:

                for j in range(len(grid[0]) - 2):
                    if isgrid([grid[0][j:j + 3], grid[1][j:j + 3], grid[2][j:j + 3]]) == True:
                        ans = ans + 1

        elif len(grid[0])==3 and len(grid)>3:
            for i in range(len(grid) - 2):


                    if isgrid([grid[i][0:3], grid[i + 1][0:3], grid[i + 2][0:3]]) == True:
                        ans = ans + 1


        elif len(grid[0])==3 and len(grid)==3:



                    if isgrid([grid[0][0:3], grid[1][0:3], grid[ 2][0:3]]) == True:
                        ans = ans + 1


        else:
            for i in range(len(grid) - 2):
                for j in range(len(grid[0]) - 2):


                    if isgrid([grid[i][j:j + 3], grid[i + 1][j:j + 3], grid[i + 2][j:j + 3]]) == True:
                        ans = ans + 1









        return ans

print(Solution().numMagicSquaresInside([[3,10,2,3,4],[4,5,6,8,1],[8,8,1,6,8],[1,3,5,7,1],[9,4,9,2,9]]))