class Solution(object):
    def intersection(self, nums1, nums2):
        a=[]
        for i in set(nums1):
            if i in set(nums2):
                a.append(i)
        return a