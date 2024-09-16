

class Solution(object):
    def addDigits(self, num):
        def digui(n):
            m=0
            while n!=0:
                m=m+(n%10)
                n=int(n/10)
            return m
        while num>=10:
            num=digui(num)
        return num



print(Solution().addDigits(10))