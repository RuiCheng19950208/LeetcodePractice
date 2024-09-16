class Solution(object):
    def groupAnagrams(self, strs):
        ans={}
        for i in strs:
            ans[tuple(sorted(i))]=[]
        for i in strs:
            ans[tuple(sorted(i))].append(i)

        return ans.values()


print(Solution().groupAnagrams( ["eat","tea","tan","ate","nat","bat"]))
print(Solution().groupAnagrams( ["eat"]))
print(Solution().groupAnagrams( ['']))