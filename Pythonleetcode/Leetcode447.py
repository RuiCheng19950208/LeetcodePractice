class Solution(object):
    def numberOfBoomerangs(self, points):
        def dis(p1,p2):
            return (p1[0]-p2[0])**2+(p1[1]-p2[1])**2
        ans1=[]
        inde=[]
        dist=[]
        result=[]
        record=0
        for i in range(len(points)-1):
            for j in range(i+1,len(points)):
                dist.append(dis(points[i],points[j]))
                inde.append([i,j])
        print(dist)
        print(inde)







print(Solution().numberOfBoomerangs([[0,0],[1,0],[2,0],[10,10]]))