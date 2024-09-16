class Solution(object):
    def generateMatrix(self, n):
        if n==0:
            return []
        ans=[[0]*n for i in range(n)]
        k=0
        state_list=['right',"down","left","up"]
        state=state_list[0]
        cur_row=0
        cur_col=0
        while k<n*n:
            k+=1
            if state=='right':
                ans[cur_row][cur_col]=k
                if cur_col+1>=n or (cur_col<n-1 and ans[cur_row][cur_col+1]>0) :
                    state=state_list[1]
                    cur_row+=1
                else:
                    cur_col+=1

            elif state=='down':
                ans[cur_row][cur_col]=k
                if cur_row+1>=n or (cur_row<n-1 and ans[cur_row+1][cur_col]>0) :
                    state=state_list[2]
                    cur_col-=1
                else:
                    cur_row+=1


            elif state=='left':
                ans[cur_row][cur_col]=k
                if cur_col<=0 or (cur_col>0 and ans[cur_row][cur_col-1]>0) :
                    state=state_list[3]
                    cur_row-=1
                else:
                    cur_col-=1


            elif state=='up':
                ans[cur_row][cur_col]=k
                if cur_row<=0 or (cur_row>0 and ans[cur_row-1][cur_col]>0) :
                    state=state_list[0]
                    cur_col+=1
                else:
                    cur_row-=1

        return ans

print(Solution().generateMatrix(1))
print(Solution().generateMatrix(2))
print(Solution().generateMatrix(3))
