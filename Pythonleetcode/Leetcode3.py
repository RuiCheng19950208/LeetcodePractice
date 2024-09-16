class Solution(object):
    def lengthOfLongestSubstring(self, s):
        if s=='':
            return 0
        start=end=0
        ans=1

        while(end!=len(s)-1):
            end=end+1

            if len(s[start:end+1])==len(list(set(s[start:end+1]))) and end-start+1>ans:
                ans = end - start + 1
            else:
                start=start+1
        return ans











print(Solution().lengthOfLongestSubstring("abcabcbb"))
print(Solution().lengthOfLongestSubstring("bbbbb"))
print(Solution().lengthOfLongestSubstring("pwwkew"))
print(Solution().lengthOfLongestSubstring("abcdefg"))