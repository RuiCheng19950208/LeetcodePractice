class Solution(object):
    def spiralOrder(self, matrix):
        if matrix==[]:
            return []
        ans=[]
        i = 0
        j = 0
        you = 1
        xia = 0
        zuo = 0
        shang = 0
        while(len(ans)!=len(matrix)*len(matrix[0])):



            if (you==1 and j==len(matrix[0])-1)or(you==1 and matrix[i][j+1]==float('inf'))  :
                you=0
                xia=1
            elif  (xia==1 and i==len(matrix)-1)or (xia==1 and matrix[i+1][j]==float('inf')):
                xia=0
                zuo=1
            elif  (zuo==1 and j==0) or (zuo==1 and matrix[i][j-1]==float('inf')):
                zuo=0
                shang=1
            elif (shang==1 and i==0)or(shang==1 and matrix[i-1][j]==float('inf')) :
                shang=0
                you=1





            if xia==1 :
                ans.append(matrix[i][j])
                matrix[i][j]=float('inf')
                i = i + 1
            elif shang==1:
                ans.append(matrix[i][j])
                matrix[i][j] = float('inf')
                i = i-1
            elif zuo==1:
                ans.append(matrix[i][j])
                matrix[i][j] = float('inf')
                j = j-1
            else:
                ans.append(matrix[i][j])
                matrix[i][j] = float('inf')
                j=j+1



        return ans




print(Solution().spiralOrder([
 [ 1, 2, 3 ],
 [ 4, 5, 6 ],
 [ 7, 8, 9 ]
]))


print(Solution().spiralOrder([
  [1, 2, 3, 4],
  [5, 6, 7, 8],
  [9,10,11,12]]
))