class Solution(object):
    def binaryGap(self, N):
        s=''
        while N!=0:
            s=str(N%2)+s
            N=N//2

        ans=1
        max=1
        if '1' not in s[1:] or s=='0':
            return 0
        for i in range(len(s)):
            if s[i]=='1':
                ans=1
            elif '1' in s[i:]:

                ans=ans+1
                if ans>max:
                    max=ans
        return max




print(Solution().binaryGap(48))