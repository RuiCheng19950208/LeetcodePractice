class Solution(object):
    def xorOperation(self, n, start):
        nums=[]
        for i in range(n):
            nums.append(start+i*2)
        ans=nums[0]
        for i in nums[1:]:
            ans=ans^i

        return ans

print(Solution().xorOperation( n = 5, start = 0))
print(Solution().xorOperation( n = 4, start = 3))
print(Solution().xorOperation( n = 1, start = 7))
print(Solution().xorOperation( n = 10, start = 5))