class Solution(object):
    def reachNumber(self, target):
        target=abs(target)
        i=0
        S=0
        while(S<target):
            i=i+1
            S=S+i

        delta=S-target
        if delta==0 or delta%2==0:
            return i
        elif (S+i+1-target)%2==0:
            return i+1
        else:
            return i+2







print(Solution().reachNumber(2))
print(Solution().reachNumber(3))
print(Solution().reachNumber(10))
print(Solution().reachNumber(13))