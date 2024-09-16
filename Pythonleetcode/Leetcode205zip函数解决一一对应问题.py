class Solution(object):
    def isIsomorphic(self, s, t):
        # print(list(set(zip(s,t))))
        return len(list(set(s)))==len(list(set(t)))==len(set(zip(s,t)))





print(Solution().isIsomorphic( "paper", "title"))
print(Solution().isIsomorphic( "egg",  "add"))
print(Solution().isIsomorphic( "foo", "bar"))
print(Solution().isIsomorphic( "abab", "baba"))