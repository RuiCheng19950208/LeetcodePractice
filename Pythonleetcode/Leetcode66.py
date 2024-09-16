class Solution(object):
    def plusOne(self, digits):
        n=0

        x=[]
        for i in range(0,len(digits)):
            n=n+digits[i]*(10**(len(digits)-i-1))
        s=str(n+1)
        for i in range(0,len(s)):
            x.append(int(s[i]))
        return x







print(Solution().plusOne([1,2,9]))