# class Solution(object):
#     def firstUniqChar(self, s):
#         """
#         :type s: str
#         :rtype: int
#         """
#         for i in range(len(s)):
#             if s.count(s[i])==1:
#                 return i
#         return -1


# Use dictionary much faster
class Solution(object):
    def firstUniqChar(self, s):
        """
        :type s: str
        :rtype: int
        """
        dict_s={}
        for i in range(len(s)):
            if s[i] not in dict_s:
                dict_s[s[i]]=1
            else:
                dict_s[s[i]] += 1


        for i in range(len(s)):
            if dict_s[s[i]]==1:
                return i
        return -1


print(Solution().firstUniqChar("leetcode"))
print(Solution().firstUniqChar("loveleetcode"))
