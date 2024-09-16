class Solution(object):
    def repeatedStringMatch(self, A, B):
        ans=A+''
        res=1
        while(len(ans)<=2*len(B) or res<=5):
            if B in ans:
                return res
            else:
                ans=ans+A
                res=res+1

        return -1


print(Solution().repeatedStringMatch("abcd","cdabcdab"))