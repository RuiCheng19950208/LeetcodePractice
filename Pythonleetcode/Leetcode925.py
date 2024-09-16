class Solution(object):
    def isLongPressedName(self, name, typed):
        fast=0
        slow=0
        if name[0]!=typed[0]:
            return False
        while slow<len(name):
            if fast>=len(typed):
                return False
            if name[slow]==typed[fast]:
                slow+=1
                fast+=1
            else:
                if name[slow-1]==typed[fast]:
                    fast+=1
                else:
                    return False

        if fast!=len(typed):
            for i in range(fast,len(typed)):
                if typed[i]!=name[-1]:
                    return False
        return True





print(Solution().isLongPressedName("alex", "aaleex"))
print(Solution().isLongPressedName("saeed", "ssaaedd"))
print(Solution().isLongPressedName("leelee", "lleeelee"))
print(Solution().isLongPressedName("laiden", "laiden"))
print(Solution().isLongPressedName("alex","aaleexa"))





