class Solution(object):
    def maxCount(self, m, n, ops):
        if ops==[]:
            return m*n
        else:
            return min(t[0] for t in ops)*min(t[1] for t in ops)

print(Solution().maxCount(3,3,[[2,2],[3,3]]))
print(Solution().maxCount(3,3,[[2,2],[3,3],[3,3],[3,3],[2,2],[3,3],[3,3],[3,3],[2,2],[3,3],[3,3],[3,3]]))
print(Solution().maxCount(3,3,[]))