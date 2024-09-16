# class Solution(object):
#     def numberOfArithmeticSlices(self, A):
#         if len(A)<3:
#             return 0
#         def istrue(s):
#
#             cha=s[1]-s[0]
#             for i in range(1, len(s)):
#                 if s[i] - s[i - 1] != cha:
#                     return False
#             return True
#         ans=0
#         for i in range(len(A)-2):
#             for j in range(i+2,len(A)):
#
#                 if istrue(A[i:j+1]):
#                     ans=ans+1
#
#         return ans
# 爆破失败

class Solution(object):
    def numberOfArithmeticSlices(self, A):
        mark=0
        start=0
        end=2
        ans=0
        if len(A)<3:
            return 0

        while( start<len(A)-2 and end<len(A)):

            if mark==0 and A[start+1]-A[start]==A[end]-A[end-1]:
                cha=A[end]-A[end-1]

                count=3
                mark=1
            elif mark==0 and A[start+1]-A[start]!=A[end]-A[end-1]:
                start=start+1
                end=end+1

            if mark==1:
                if end==len(A)-1:
                    ans = ans + ((count - 1) * (count - 2)) / 2
                    return int(ans)

                end=end+1

                if A[end]-A[end-1]==cha:
                    count=count+1
                    if end==len(A)-1:

                        ans=ans+((count-1)*(count-2))/2
                        return int(ans)


                else:
                    mark=0
                    ans=ans+((count-1)*(count-2))/2
                    start=end+0
                    end=start+2

        return int(ans)








print(Solution().numberOfArithmeticSlices([1, 1, 2, 5, 7]))
print(Solution().numberOfArithmeticSlices([1, 3, 5, 7, 9]))
print(Solution().numberOfArithmeticSlices([7,7,7,7]))
print(Solution().numberOfArithmeticSlices([3, -1, -5, -9]))
print(Solution().numberOfArithmeticSlices([1, 2,3]))



