class Solution(object):
    def countConsistentStrings(self, allowed, words):
        ans=0
        for i in words:
            for j in i:
                if j in allowed:
                    pass
                else:
                    ans-=1
                    break
            ans+=1


        return ans

print(Solution().countConsistentStrings(allowed = "ab", words = ["ad","bd","aaab","baa","badab"]))
print(Solution().countConsistentStrings(allowed = "abc", words = ["a","b","c","ab","ac","bc","abc"]))
print(Solution().countConsistentStrings(allowed = "cad", words = ["cc","acd","b","ba","bac","bad","ac","d"]))
