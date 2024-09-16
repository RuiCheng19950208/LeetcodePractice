class Solution(object):
    def hasAlternatingBits(self, n):
        def erjin(n):
            ans=[]
            while(n!=0):
                yushu=n%2
                n=int(n/2)
                ans.append(yushu)
            result=0
            for i in range(len(ans)):
                result=result+(10**i)*ans[i]
            return result

        test=str(erjin(n))
        for i in range(len(test)-1):
            if test[i]==test[i+1]:
                return False


        return True








print(Solution().hasAlternatingBits(5))
print(Solution().hasAlternatingBits(7))
print(Solution().hasAlternatingBits(11))
print(Solution().hasAlternatingBits(10))