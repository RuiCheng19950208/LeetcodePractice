class Solution(object):
    def thirdMax(self, nums):
        nums=sorted(list(set(nums)))
        if len(nums)<3:
            return nums[-1]
        else:
            return nums[-3]




print(Solution().thirdMax([2, 2,4, 3, 1]))