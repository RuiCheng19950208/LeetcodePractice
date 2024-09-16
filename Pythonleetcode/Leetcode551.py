
# Old approach
# class Solution(object):
#     def checkRecord(self, s):
#         A = 0
#         L = 0
#         if s[0]=='A':
#             A=A+1
#
#         for i in range(1,len(s)):
#             if s[i]=='A':
#                 A=A+1
#                 L=0
#             elif s[i]=='P':
#                 L=0
#             elif s[i]=='L' and s[i-1]=='L':
#                 L=L+1
#                 if L>1:
#                     return False
#         if A>1:
#             return False
#         else:return True


class Solution(object):
    def checkRecord(self, s):
        if s.count('A')>1 :
            return False
        else:
            for i in range(len(s)-2):
                if s[i]=='L' and s[i+1]=='L' and s[i+2]=='L' :
                    return False
            return True




print(Solution().checkRecord("PPALL"))

