import copy
class Solution(object):
    def minimumTotal(self, triangle):
        mi=[0]*len(triangle[len(triangle)-1])
        mi[0]=triangle[0][0]
        for i in range(1,len(triangle)):
            co=copy.deepcopy(mi)
            for j in range(len(triangle[i])):
                if j==0:
                    mi[j]=co[j]+triangle[i][j]
                elif j == len(triangle[i])-1:
                    mi[j] = co[j-1] + triangle[i][j]
                else:
                    mi[j]=triangle[i][j]+min(co[j],co[j-1])
            # print(mi)
             

        return min(mi)







print(Solution().minimumTotal([
     [2],
    [3,4],
   [6,5,7],
  [4,1,8,3]
]))