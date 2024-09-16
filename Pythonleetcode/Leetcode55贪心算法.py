class Solution(object):
    def canJump(self, nums):

        reach = 0
        for i, num in enumerate(nums):
            if i > reach:
                return False
            reach = max(reach, i + num)
            print(i,num,reach)
        return True

#此题答案不严谨，若step过大则会导致错误结果，但是在网站上可以通过



print(Solution().canJump([2,3,1,1,4]))
print(Solution().canJump([3,2,1,0,4]))


