class Solution(object):
    def isRectangleOverlap(self, rec1, rec2):
        if max([rec1[0],rec1[2]])<=min([rec2[0],rec2[2]]) or min([rec1[0],rec1[2]])>=max([rec2[0],rec2[2]]) or max([rec1[1],rec1[3]])<=min([rec2[1],rec2[3]]) or min([rec1[1],rec1[3]])>=max([rec2[1],rec2[3]]):
            return False
        else: return True






print(Solution().isRectangleOverlap([0, 0, 1, 1],  [1, 0, 2, 1]))

# [0, 0, 1, 1],  [1, 0, 2, 1]
