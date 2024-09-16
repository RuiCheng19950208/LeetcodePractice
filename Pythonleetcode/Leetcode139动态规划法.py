class Solution(object):
    def wordBreak(self, s, wordDict):
        ls=len(s)
        m=[False]*(ls+1)
        m[0]=True
        for i in range(1,len(s)+1):
            for word in wordDict:

                if s[i-len(word):i]== word  and m[i-len(word)]:
                    m[i]=True

        return m[-1]




print(Solution().wordBreak( "leetcode",  ["leet", "code"]))
print(Solution().wordBreak("applepenapple", ["apple", "pen"]))
print(Solution().wordBreak("catsandog", ["cats", "dog", "sand", "and", "cat"]))