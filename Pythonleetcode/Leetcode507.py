class Solution(object):
    def checkPerfectNumber(self, num):
        ans=1
        if num<=0:
            return False
        if num**0.5-int(num**0.5)==0:
            ans=ans+int(num**0.5)
        for i in range(2,int(num**0.5)+1):
            if num%i==0:
                ans=ans+i+(num//i)



        return ans==num



print(Solution().checkPerfectNumber(6))