class Solution(object):
    def largestTriangleArea(self, points):
        res = 0
        N = len(points)
        for i in range(N - 2):
            for j in range(i + 1, N - 1):
                for k in range(i + 2, N):
                    (x1, y1), (x2, y2), (x3, y3) = points[i], points[j], points[k]
                    res = max(res, 0.5 * abs(x1 * (y2 - y3) + x2 * (y3 - y1) + x3 * (y1 - y2)))
        return res






print(Solution().largestTriangleArea([[0,0],[0,1],[1,0],[0,2],[2,0]]))