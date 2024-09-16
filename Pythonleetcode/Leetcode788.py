class Solution(object):
    def rotatedDigits(self, N):

        def haoshu(n):
            s=str(n)
            a=0
            for i in range(len(s)):
                    if (s[i] == '1' or s[i] == '0'  or s[i] == '8'):
                        continue

                    if  (s[i] == '2' or s[i] == '5' or s[i] == '6' or s[i] == '9'):
                        a=a+1
                        continue
                    if (s[i] == '3' or s[i] == '4' or s[i] == '7'):
                        return False
            if a==0:
                return False


            return True

        ans=0
        for i in range(1,N+1):
            if haoshu(i)==True:
                ans=ans+1


        return ans

print(Solution().rotatedDigits(857))