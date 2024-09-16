class Solution(object):
    def removeDuplicates(self, s):
        if len(s)<2:
            return s
        ans=s[0]
        for i in s[1:]:
            # print(ans,i)
            if len(ans)!=0 and i==ans[-1]:
                ans=ans[:len(ans)-1]
            else:
                ans= ans+i
        return ans
print(Solution().removeDuplicates("abbaca"))
