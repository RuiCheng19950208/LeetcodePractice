class Solution(object):
    def largestPerimeter(self, A):
        A=sorted(A)[::-1]
        for i in range(len(A)-2):
            if A[i]<A[i+1]+A[i+2]:
                return A[i]+A[i+1]+A[i+2]

        return 0







print(Solution().largestPerimeter([3,2,3,4]))
print(Solution().largestPerimeter([3,6,2,3]))
print(Solution().largestPerimeter([2,1,2]))

