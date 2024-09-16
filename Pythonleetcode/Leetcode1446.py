class Solution(object):
    def maxPower(self, s):
        ans=1
        record=1
        if len(s)==0:
            return 0
        for i in range(1,len(s)):
            if s[i]==s[i-1]:
                ans+=1
                if ans>record:
                    record=ans
            else:
                ans=1

        return record
print(Solution().maxPower(s = "leetcode"))