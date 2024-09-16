class Solution(object):
    def isPowerOfTwo(self, n):
        if n<=0:
            return False
        s=''
        while n!=0:
            s=str(n%2)+s
            n=n//2
        if '1' not in s[1:]:
            return True
        else: return  False