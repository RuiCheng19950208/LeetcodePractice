class Solution(object):
    def minOperations(self, n):
        half_length=n//2

        if n%2==1:
            ans = 0
            for i in range(1,half_length + 1):
                ans += i*2
            return ans

        else:
            ans = 0
            for i in range(1,half_length + 1):
                ans += i*2-1
            return ans


print(Solution().minOperations(3))
print(Solution().minOperations(6))