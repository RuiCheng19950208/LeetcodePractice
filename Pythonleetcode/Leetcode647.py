# class Solution(object):
#     def countSubstrings(self, s):
#
#         count = 0
#         for i in range(len(s)):
#             for j in range(i, len(s)):
#                 if s[i:j + 1] == s[i:j + 1][::-1]:
#                     count += 1
#         return count
#暴破可行


class Solution(object):
    def countSubstrings(self, s):
        ans=0
        l=len(s)
        for i in range(1,len(s)-1):
            left=i+0
            right=i+0
            while(1):
                left=left-1
                right=right+1
                if left<0 or right>l-1:
                    break
                elif s[left:right+1]==s[left:right+1][::-1]:
                    ans=ans+1

        for i in range(1,len(s)):
            left=i+0
            right=i-1
            while(1):
                left=left-1
                right=right+1
                if left<0 or right>l-1:
                    break
                elif s[left:right+1]==s[left:right+1][::-1]:
                    ans=ans+1

        return ans+l

#理论上会比爆破快的方法，实际上慢了









print(Solution().countSubstrings("abc"))
print(Solution().countSubstrings("aaa"))