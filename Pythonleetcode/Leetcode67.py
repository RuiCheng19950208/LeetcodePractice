# class Solution(object):
#
#
#     def TwotoTen(self,x):
#         c = str(x)
#
#         n = 0
#         for i in range(0, len(c) ):
#             if c[i]=='1':
#                 n = n +2**(len(c)-i-1)
#                 print(n)
#             else: n=n+0
#         return n
#
#     def TentoTwo(self, x):
#         result=''
#         while True:
#             if x!=0:
#                 result=result+str(x%2)
#                 x=x//2
#             else: break
#
#         return result[::-1]
#
#
#
#
#
#
#
#
#     def addBinary(self, a, b):
#         if a=='0' and b=='0':
#             return '0'
#
#         return self.TentoTwo(self.TwotoTen(a) + self.TwotoTen(b))

class Solution(object):
    def addBinary(self, a, b):
        #eval将字符串变为数字
        return bin(eval('0b' + str(a)) + eval('0b' + str(b)))[2:]




print(Solution().addBinary(1,11))






