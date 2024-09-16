class Solution:
    def moveZeroes(self, nums):

        n = nums.count(0)
        for i in range(n):
            nums.remove(0)
        nums.extend([0]*n)

        return nums






print(Solution().moveZeroes([0,1,0,3,12]))