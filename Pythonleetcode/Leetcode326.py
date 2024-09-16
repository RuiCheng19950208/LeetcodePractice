class Solution(object):
    def isPowerOfThree(self, n):
        if n<=0:
            return False
        s=''
        while n!=0:
            s=str(n%3)+s
            n=n//3
        print(s)

        if ('1' not in s[1:]) and ('2' not in s[1:]) and s[0]=='1':
            return True
        else: return  False



print(Solution().isPowerOfThree(9))