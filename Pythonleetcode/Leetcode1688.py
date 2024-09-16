class Solution(object):
    def numberOfMatches(self, n):
        ans=0
        while n!=1:
            if n%2==1:
                ans += n // 2
                n=n//2+1

            else:
                ans += n // 2
                n=n//2
        return ans



print(Solution().numberOfMatches(7))
print(Solution().numberOfMatches(14))