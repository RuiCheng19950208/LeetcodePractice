class Solution(object):
    def solve(self, board):
        alive=[]
        for i in range(len(board)):
            for j in range(len(board[0])):
                if (i==0 or i==len(board)-1) and (j==0 or j==len(board[0])-1) and board[i][j]=='O':
                    alive.append([i,j])
                    
        def live(alive,board,i,j):

            return board


        board=live(alive,board)








print(Solution().solve([['X','X','X','X'],
                        ['X','O','O','X'],
                        ['X','X','O','X'],
                        ['X','O','X','X']]))