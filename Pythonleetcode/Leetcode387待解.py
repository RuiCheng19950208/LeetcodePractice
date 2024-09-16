class Solution(object):
    def firstUniqChar(self, s):

        for i in range(0,len(s)):

                if s.count(s[i])==1:
                    return i






        return -1



print(Solution().firstUniqChar("dddccdbba"))