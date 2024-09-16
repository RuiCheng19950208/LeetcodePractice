class Solution(object):
    def dominantIndex(self, nums):
        if len(nums)==1:
            return 0
        nums1=sorted(nums)
        if (nums1[-1]>0 and nums1[-2]==0) or nums1[-1]/nums1[-2]>=2 :
            return nums.index(nums1[-1])
        else: return -1



print(Solution().dominantIndex([3, 6, 1, 0]))

print(Solution().dominantIndex([0, 0, 1, 0]))