class Solution(object):
    def canIWin(self, maxChoosableInteger, desiredTotal):
        if desiredTotal<=maxChoosableInteger:
            return True
        elif desiredTotal%(maxChoosableInteger+1)==0:
            return False
        else:
            return True




print(Solution().canIWin(10,11))