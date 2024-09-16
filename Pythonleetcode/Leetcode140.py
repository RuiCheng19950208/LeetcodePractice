class Solution(object):
    def wordBreak(self, s, wordDict):
        def wordBreak_sub(s_start,s_end,wordDict):
            for i in range(len(s_start)):
                s_end=s_start[-1]+s_end
                s_start=s_start[:len(s_start)-1]
                print(s_start,s_end)
                if s_end in wordDict:
                    if s_start in wordDict:
                        return s_start+" "+s_end
                    else:
                        return wordBreak_sub(s_start,"", wordDict)+" "+s_end
            return ""

        ans=[]
        s_start=s
        s_end=""
        for i in range(len(s)):
            s_end = s_start[-1] + s_end
            s_start = s_start[:len(s_start) - 1]
            ans.append(wordBreak_sub(s_start,s_end,wordDict))
        print(ans)
        ans_2=[]
        for i in ans:
            if len(i)>0:
                ans_2.append(i)
        print(ans_2)
        return ans_2



print(Solution().wordBreak(s = "catsanddog",wordDict = ["cat", "cats", "and", "sand", "dog"]))
print(Solution().wordBreak(s = "pineapplepenapple",wordDict = ["apple", "pen", "applepen", "pine", "pineapple"]))
print(Solution().wordBreak(s = "catsandog",wordDict = ["cats", "dog", "sand", "and", "cat"]))

