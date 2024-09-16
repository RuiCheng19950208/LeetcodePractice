# class Solution(object):
#     def lengthOfLastWord(self, s):
#         if s=='':
#             return 0
#         if len(s)==1:
#             if s==' ':
#                 return 0
#             else:
#                 return 1
#         ans=0
#         res=[]
#         for i in range(0,len(s)):
#             if s[i]!=' ':
#                 ans=ans+1
#                 res.append(ans)
#             else:
#                 ans=0
#                 res.append(ans)
#
#         k=-1
#         while res[k]==0:
#             if k==-len(s):
#                 return 0
#             k=k-1
#
#
#         return res[k]


class Solution(object):
    def lengthOfLastWord(self, s):
        s=s.split()
        if len(s)==0:
            return 0
        return len(s[-1])



print(Solution().lengthOfLastWord('a '))