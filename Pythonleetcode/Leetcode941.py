class Solution(object):
    def validMountainArray(self, A):
        if len(A)<3:
            return False
        start=0
        end=len(A)-1
        while start!=end:
            if A[start+1]>A[start]:
                start=start+1
            elif A[end-1]>A[end]:
                end=end-1
            else: return False
        if start!=0 and end!=len(A)-1:
            return True
        else:return False








print(Solution().validMountainArray([2,1]))
print(Solution().validMountainArray([3,5,5]))
print(Solution().validMountainArray([0,3,2,1]))
