class Solution(object):
    def isAnagram(self, s, t):
        ta=[]
        tb=[]
        if len(s)!=len(t):
            return False
        for i in range(len(s)):
            ta.append(s[i])
            tb.append(t[i])
        if sorted(ta)==sorted(tb):
            return True
        else:return False




print(Solution().isAnagram( "ab", "bb"))