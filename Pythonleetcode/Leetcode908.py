class Solution(object):
    def smallestRangeI(self, A, K):
        A.sort()
        if A[0]+K<A[-1]-K:
            return A[-1]-A[0]-(2*K)
        else:
            return 0



print(Solution().smallestRangeI([0,10],2))