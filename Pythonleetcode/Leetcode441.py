class Solution(object):
    def arrangeCoins(self, n):
        ans=int(n**0.5)
        i=int(n**0.5)
        n=n-(i*(i+1))/2
        while n>i:
            i=i+1
            n=n-i
            ans=ans+1
        return ans







print(Solution().arrangeCoins(1))
