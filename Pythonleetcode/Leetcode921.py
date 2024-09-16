class Solution(object):
    def minAddToMakeValid(self, S):


        if S=='':
            return 0
        ans=1
        balance = 0
        if S[0]=='(':
            mark = 0
            balance=1
        else:
            mark=1
            balance = -1

        for i in range(1,len(S)):
            # print(ans)
            if S[i]=='(' and balance<0:
                ans=ans+1
                mark=0
                balance=1

            elif S[i]=='(' and balance>=0:
                ans=ans+1
                mark=0
                balance=balance+1



            elif mark==0 and ans==1 and balance>0:
                ans=ans-1
                mark=1
                balance = balance -1
            elif mark==0 and ans==1 and balance<=0:
                ans=ans+1
                mark=1
                balance = balance - 1


            elif mark == 0 and balance>0:

                ans=ans-1
                balance = balance - 1
            elif mark == 0 and balance<=0:
                mark=1
                ans=ans+1
                balance = balance - 1
            else:
                ans = ans +1
                balance = balance - 1
        return ans





print(Solution().minAddToMakeValid("()))(("))#4
print(Solution().minAddToMakeValid("())"))#1
print(Solution().minAddToMakeValid("((("))#3
print(Solution().minAddToMakeValid("((())"))#1

print(Solution().minAddToMakeValid(")())("))#3


print(Solution().minAddToMakeValid(")))())"))#4

print(Solution().minAddToMakeValid(")()"))#1


print(Solution().minAddToMakeValid("()))))(())))()"))#6
#
#
#
#


