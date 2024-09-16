class Solution(object):
    def isValidSudoku(self, board):

        def chongfu(matrix):
            num=[]
            for i in matrix:
                if i!='.':
                    num.append(i)
            if len(num)==len(list(set(num))):
                return True
            else: return False

        for i in board:   #判断行重复
            if chongfu(i)==False:
                return  False

        remake=[[],[],[],[],[],[],[],[],[]]
        k=0
        for i in range(0,9):
            for j in range(0, 9):
                k=((i//3)*3)+(j//3) #完美的切割矩阵方法

                remake[k].append(board[i][j])  #判断3x3方格重复

        for i in remake:
            if chongfu(i)==False:
                return  False

        remake = [[], [], [], [], [], [], [], [], []]

        for i in range(0, 9):
            for j in range(0, 9):


                remake[j].append(board[i][j])

        for i in remake: #判断列重复
            if chongfu(i) == False:
                return False

        return True





print(Solution().isValidSudoku([
  ["5","3",".",".","7",".",".",".","."],
  ["6",".",".","1","9","5",".",".","."],
  [".","9","8",".",".",".",".","6","."],
  ["8",".",".",".","6",".",".",".","3"],
  ["4",".",".","8",".","3",".",".","1"],
  ["7",".",".",".","2",".",".",".","6"],
  [".","6",".",".",".",".","2","8","."],
  [".",".",".","4","1","9",".",".","5"],
  [".",".",".",".","8",".",".","7","9"]
]
))