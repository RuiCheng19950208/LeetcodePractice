
class Solution(object):
    def findComplement(self, num):
        for i in range(1000):
            if 2**i>num:
                return 2 ** i-1-num









print(Solution().findComplement(5))