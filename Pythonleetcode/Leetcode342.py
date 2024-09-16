class Solution(object):
    def isPowerOfFour(self, num):
        for i in range(0,100):
            if 4**i==num:
                return True
        return False



print(Solution().isPowerOfFour(16))