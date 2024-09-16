class Solution:
    def reverseBits(self, n):
        ans=0
        def erjin(n):
            ans=''
            while(1):
                ans=str(n%2)+ans
                n=int(n/2)
                if n==0:
                    break
            return ans
        ans=erjin(n)
        while (1):
            if len(ans) != 32:
                ans = '0' + ans
            else:
                break
        result=0
        for i in range(len(ans)):
            result=result+(2**i)*int(ans[i])
        return result


print(Solution().reverseBits(43261596))