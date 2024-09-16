class Solution(object):
    def integerBreak(self, n):
        if n==2:
            return 1
        elif n==3:
            return 2
        else:
            ans=1
            while(n!=0):
                if n==4:
                    return ans*4
                if n==2:
                    return ans*2
                if n==3:
                    return ans*3
                else: n=n-3
                ans=ans*3





print(Solution().integerBreak(2))
print(Solution().integerBreak(10))