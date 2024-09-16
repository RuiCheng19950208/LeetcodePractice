class Solution(object):
    def sortedSquares(self, A):
        for i in range(len(A)):
            A[i] = A[i] ** 2
        return sorted(A)


print(Solution().sortedSquares([-4,-1,0,3,10]))
print(Solution().sortedSquares([-7,-3,2,3,11]))