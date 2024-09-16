class Solution(object):
    def checkRecord(self, n):
        if n == 0:
            return 0
        if n == 1:
            return 3
        if n == 2:
            return 8

        ans = [1, 2, 4]
        for i in range(3, n+1):
            ans.append((ans[i - 3] + ans[i - 2] + ans[i - 1])%(10**9+7))
        res=ans[-1]
        for i in range(0,n):
            res= res+ans[i]*ans[n-1-i]%(10**9+7)

        return res%(10**9+7)



print(Solution().checkRecord(2))
print(Solution().checkRecord(3))
print(Solution().checkRecord(4))
print(Solution().checkRecord(5))