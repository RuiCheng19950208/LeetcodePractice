class Solution(object):
    def trailingZeroes(self, n):
        ans=0
        while n!=0:
            n=n//5
            ans=ans+n
        return ans


print(Solution().trailingZeroes(2500))