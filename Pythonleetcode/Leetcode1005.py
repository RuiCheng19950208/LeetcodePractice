class Solution(object):
    def largestSumAfterKNegations(self, A, K):
        """
        :type A: List[int]
        :type K: int
        :rtype: int
        """
        A.sort()
        for i in range(K):
            A[0] = -A[0]
            A.sort()
        return sum(A)

print(Solution().largestSumAfterKNegations(A = [4,2,3], K = 1))
print(Solution().largestSumAfterKNegations( A = [3,-1,0,2], K = 3))
print(Solution().largestSumAfterKNegations(A = [2,-3,-1,5,-4], K = 2))


