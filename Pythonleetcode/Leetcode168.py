class Solution(object):
    def convertToTitle(self, n):
        ans=""
        while n>0:
            n-=1
            remainder=n%26
            ans = ans + chr(remainder + ord("A"))
            n = n // 26

        return ans[::-1]


print(Solution().convertToTitle(28))
print(Solution().convertToTitle(27))
print(Solution().convertToTitle(26))
print(Solution().convertToTitle(26*26*26))