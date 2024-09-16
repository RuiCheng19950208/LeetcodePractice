class Solution(object):
    def pathsWithMaxScore(self, board):
        modulo=10**9+7
        ans=0
        dp=[]
        col=len(board[0])
        row=len(board)
        for i in range(row):
            temp=[]
            for j in range(col):
                temp.append([0,0])
            dp.append(temp)
        # print(dp)
        for i in range(row-1,-1,-1):
            for j in range(col-1,-1,-1):
                if board[i][j]=="X" :
                    dp[i][j]=[0,0]
                elif board[i][j]=="S":
                    dp[i][j] = [0, 1]
                elif i == row - 1  :
                    if dp[i][j+1][1]==1:
                        dp[i][j] = [dp[i][j+1][0]+int(board[i][j]),1]
                    else:
                        dp[i][j]=[0,0]
                elif j==col-1:
                    if dp[i+1][j][1]==1:
                        dp[i][j] = [dp[i+1][j][0]+int(board[i][j]),1]
                    else:
                        dp[i][j]=[0,0]
                else:
                    max_number=max(dp[i+1][j+1][0],dp[i+1][j][0],dp[i][j+1][0])
                    if dp[i+1][j+1][0]==max_number:
                        dp[i][j][1]+=dp[i+1][j+1][1]
                    if dp[i+1][j][0]==max_number:
                        dp[i][j][1]+=dp[i+1][j][1]
                    if dp[i][j+1][0]==max_number:
                        dp[i][j][1]+=dp[i][j+1][1]
                    if dp[i][j][1]!=0:
                        if board[i][j]=="E":
                            dp[i][j][0]=max_number
                        else:
                            dp[i][j][0] = int(board[i][j]) + max_number
        # print(dp)
        return [dp[0][0][0]%modulo,dp[0][0][1]%modulo]


# print(Solution().pathsWithMaxScore(["E23","2X2","12S"]))
# print(Solution().pathsWithMaxScore(["E12","1X1","21S"]))
# print(Solution().pathsWithMaxScore(["E11","XXX","11S"]))
print(Solution().pathsWithMaxScore(["E713399729","X151558988","5545833573","4366595255","23493768X9","8X24154768","1357922244","8921993297","8699512769","214631X17S"]))



