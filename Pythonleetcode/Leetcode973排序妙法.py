class Solution(object):
    def kClosest(self, points, K):
        return sorted(points, key=lambda p: p[0] ** 2 + p[1] ** 2)[:K] #排序方法key=lambda x:x[0]




print(Solution().kClosest( [[1,3],[-2,2]], 1))
print(Solution().kClosest( [[3,3],[5,-1],[-2,4]], 2))