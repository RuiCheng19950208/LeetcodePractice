class Solution(object):
    def stringMatching(self, words):
        words.sort(key=lambda x: len(x))
        ans=[]
        for i in range(len(words)):
            for j in words[i+1:]:
                if words[i] in j:
                    ans.append(words[i])
                    break

        return ans


print(Solution().stringMatching(["mass","as","hero","superhero"]))
print(Solution().stringMatching(["leetcode","et","code"]))
print(Solution().stringMatching(["blue","green","bu"]))