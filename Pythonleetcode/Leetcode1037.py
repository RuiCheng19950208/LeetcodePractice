class Solution(object):
    def isBoomerang(self, points):
        """
        :type points: List[List[int]]
        :rtype: bool
        """

        if (points[0][1]-points[1][1])*(points[0][0]-points[2][0])!=(points[0][1]-points[2][1])*(points[0][0]-points[1][0]):
            return True
        else:
            return False




print(Solution().isBoomerang([[1,1],[2,3],[3,2]]))
print(Solution().isBoomerang([[1,1],[2,2],[3,3]]))