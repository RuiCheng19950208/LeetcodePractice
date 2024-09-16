class Solution(object):
    def peakIndexInMountainArray(self, A):
        for i in range(0, len(A)):
            if A[i + 1] < A[i]:
                return i
