class Solution(object):
    def numberOfSteps (self, num):
        ans=0
        while True:

            if num%2==0 and num!=0:
                ans = ans + 1
                num=num/2
            elif num%2==1:
                ans = ans + 1
                num=num-1
            elif num==0:
                break

        return ans



print(Solution().numberOfSteps(14))
print(Solution().numberOfSteps(8))
print(Solution().numberOfSteps(123))
