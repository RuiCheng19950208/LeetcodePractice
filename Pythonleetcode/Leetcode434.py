# class Solution(object):
#     def countSegments(self, s):
#
#         if s=='':
#             return 0
#         if s==' ':
#             return 0
#         ans=1
#
#         for i in range(1,len(s)):
#             if s[i]==' ' and s[i-1] != ' ':
#                 ans=ans+1
#
#
#         if s[-1]==' ':
#             ans=ans-1
#
#         return ans

class Solution(object):
    def countSegments(self, s):
        s = s.split()
        return len(s)


print(Solution().countSegments("Of all the gin joints in all the towns in all the world,   "))