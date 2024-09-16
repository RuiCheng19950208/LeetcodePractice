class Solution(object):
    def repeatedSubstringPattern(self, s):

        return s in (s * 2)[1:-1]





print(Solution().repeatedSubstringPattern("aba"))