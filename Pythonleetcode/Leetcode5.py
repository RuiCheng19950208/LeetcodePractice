class Solution(object):
    def longestPalindrome(self, s):
        def long(s,r,l):
            while(r<len(s) and l>=0 and s[l]==s[r]):
                r=r+1
                l=l-1

            return r-l-1

        end=start=0
        for i in range(len(s)):
            l1=long(s,i,i)
            l2=long(s,i+1,i)

            maxlen=max(l1,l2)

            if maxlen > end - start + 1:
                start = i - (maxlen - 1) // 2

                end = i + maxlen // 2

        return s[start: end + 1]








print(Solution().longestPalindrome("babad"))
print(Solution().longestPalindrome("cbbd"))
print(Solution().longestPalindrome("abcba"))