class Solution(object):
    def isUgly(self, num):
        if num<=0:
            return False
        if num==1:
            return True
        while num!=1:

            if num%2==0:
                num=num//2
            elif num%3==0:
                num=num//3
            elif num%5==0:
                num=num//5
            else: return False
        return True





print(Solution().isUgly(-2147483648))