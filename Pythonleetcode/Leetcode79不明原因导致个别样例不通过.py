class Solution(object):
    def exist(self, board, word):
        def crcr(board,word,i,j):
            if word=='':
                return 1
            if j+1<len(board[0]) and board[i][j+1]==word[0]:
                j=j+1
                board[i][j]='.'
                if  crcr(board,word[1:],i,j)==1:
                    return 1

                board[i][j] = word[0]
                j=j-1

            if j-1>=0 and board[i][j-1]==word[0]:
                j = j - 1
                board[i][j] = '.'
                if  crcr(board,word[1:],i,j)==1:
                    return 1
                board[i][j] = word[0]
                j=j+1

            if i - 1 >= 0 and board[i-1][j] == word[0]:
                i = i - 1
                board[i][j] = '.'
                if  crcr(board,word[1:],i,j)==1:
                    return 1
                i=i+1
                board[i][j] = word[0]

            if i+ 1 < len(board) and board[i+1][j] == word[0]:
                i = i + 1
                board[i][j] = '.'
                if  crcr(board,word[1:],i,j)==1:
                    return 1
                board[i][j] = word[0]
                i=i-1

        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j]==word[0]:
                    board[i][j]='.'
                    a=crcr(board,word[1:],i,j)

                    if a==1:
                        return True


                    board[i][j]=word[0]




        return False


print(Solution().exist([
  ['A','B','C','E'],
  ['S','F','C','S'],
  ['A','D','E','E']
],"ABCCED"))
#




print(Solution().exist([
  ['A','B','C','A'],
  ['A','A','C','B'],
  ['A','A','C','A']
],'ABCB'))

print(Solution().exist(
[["b","a","a","b","a","b"],
 ["a","b","a","a","a","a"],
 ["a","b","a","a","a","b"],
 ["a","b","a","b","b","a"],
 ["a","a","b","b","a","b"],
 ["a","a","b","b","b","a"],
 ["a","a","b","a","a","b"]],
"aabbbbabbaababaaaabababbaaba"))



