class Solution(object):
    def findNthDigit(self, n):
        dig = 1
        while n > 10 ** (dig - 1) * 9 * dig:
            n = n - 10 ** (dig - 1) * 9 * dig #减去低位数数字占据的位数
            dig = dig + 1 #计算位数

        a = n // dig
        b = n % dig

        print(a,b,dig)

        if b != 0:
            ans = str(10 ** (dig - 1) + a)[b - 1]

        else:
            ans = str(10 ** (dig - 1) + a - 1)[::-1][b]

        return int(ans)





print(Solution().findNthDigit(100000))
print(Solution().findNthDigit(20))