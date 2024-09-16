class Solution(object):
    def judgeSquareSum(self, c):
        if c==0:
            return True
        for i in range(1,int(c**0.5)+1):
                if (int((c-i**2)**0.5))**2 == c-i**2:
                    return True
        return False




print(Solution().judgeSquareSum(10))