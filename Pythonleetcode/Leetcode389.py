class Solution(object):
    def findTheDifference(self, s, t):
        for i in set(t):
            if t.count(i)!=s.count(i):
                return i






print(Solution().findTheDifference('abcd','abcde'))