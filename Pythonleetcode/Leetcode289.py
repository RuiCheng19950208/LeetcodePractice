class Solution(object):
    def gameOfLife(self, board):
        """
        :type board: List[List[int]]
        :rtype: None Do not return anything, modify board in-place instead.
        """
        def live_or_die(board,i,j):
            count_1=0
            for k in range(max([0,i-1]),min([len(board),i+2])):
                for w in range(max([0, j - 1]), min([len(board[0]), j + 2])):

                    if board[k][w]==1 and not (k==i and w==j):
                        print([i, j], [k, w], board[k][w])
                        count_1 +=1
            print(count_1)
            if count_1<2:
                return 0
            elif count_1 == 2 and board[i][j]==1:
                return 1
            elif count_1 == 2 and board[i][j]==0:
                return 0
            elif count_1==3:
                return 1
            elif count_1>3:
                return 0
        board_ans =[]
        for i in range(len(board)):
            board_ans.append([0]*len(board[0]))

        for i in range(len(board)):
            for j in range(len(board[0])):
                board_ans[i][j] = live_or_die(board,i,j)
        for i in range(len(board)):
            for j in range(len(board[0])):
                board[i][j]=board_ans[i][j]
        return board







print(Solution().gameOfLife([
  [0,1,0],
  [0,0,1],
  [1,1,1],
  [0,0,0]
]))