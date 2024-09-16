class Solution(object):
    def isMonotonic(self, A):
        if A==sorted(A) or A==sorted(A)[::-1]:
            return True
        else:
            return False



print(Solution().isMonotonic([1,2,2,3]))
print(Solution().isMonotonic([6,5,4,4]))
print(Solution().isMonotonic([1,3,2]))