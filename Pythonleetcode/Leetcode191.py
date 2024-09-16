class Solution(object):
    def hammingWeight(self, n):
        ans=0
        while n!=0:
            ans=ans+(n%2)
            n=n//2




        return ans

print(Solution().hammingWeight(7))