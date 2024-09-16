class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        nums=sorted(nums1+nums2)
        if len(nums)%2==0:
            ans=(nums[int(len(nums)/2)-1]+nums[int(len(nums)/2)])/2.0
        else:
            ans = nums[int(len(nums)/2)]
        return ans

print(Solution().findMedianSortedArrays(nums1 = [1,3], nums2 = [2]))
print(Solution().findMedianSortedArrays(nums1 = [1,2], nums2 = [3,4]))
