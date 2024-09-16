# class Solution(object):
#     def repeatedNTimes(self, A):
#         B=sorted(list(set(A)))
#         for i in range(len(B)):
#             if A.count(B[i])==len(A)/2:
#                 return B[i]
#超时


class Solution(object):
    def repeatedNTimes(self, A):
        B=sorted(A)
        i=int(len(B)/2)
        if B[0]==B[i-1]:
            return B[0]
        if B[i]==B[-1]:
            return B[-1]
        if B[i-1]==B[i]:
            return B[i]







print(Solution().repeatedNTimes([1,2,3,3]))
print(Solution().repeatedNTimes([2,1,2,5,3,2]))
print(Solution().repeatedNTimes([5,1,5,2,5,3,5,4]))