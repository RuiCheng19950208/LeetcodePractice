class Solution(object):
    def convertToBase7(self, num):
        if num==0:
            return '0'

        b=''
        zheng=0
        if num<0:
            zheng=1
            num=0-num
        while num!=0:
            b=str(num%7)+b
            num=num//7
        if zheng==1:
            b= '-'+b


        return b



print(Solution().convertToBase7(-7))