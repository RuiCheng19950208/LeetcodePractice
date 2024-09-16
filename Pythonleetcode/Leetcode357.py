class Solution(object):
    def countNumbersWithUniqueDigits(self, n):
        def fract(n):
            ans=1
            for i in range(1,n+1):
                ans=ans*i
            return ans
        ans=0
        if n==0:
            return 1
        for i in range(1,n+1):
            if i==1:
                ans+=10
            else:
                ans+=9*(fract(9)/fract(9-i+1))
        return int(ans)





print(Solution().countNumbersWithUniqueDigits(2))
print(Solution().countNumbersWithUniqueDigits(3))
