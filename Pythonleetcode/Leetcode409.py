class Solution(object):
    def longestPalindrome(self, s):
        ans=0
        a=(list(set(s)))
        max=0
        for i in a:
            b=s.count(i)
            if b%2==0:
                ans=ans+b

            else:
                ans=ans+b-1
                max=1
        ans=ans+max
        return ans






print(Solution().longestPalindrome("abbcccddddfffff"))
print(Solution().longestPalindrome("abccccdd"))