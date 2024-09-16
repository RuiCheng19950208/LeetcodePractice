class Solution(object):
    def intersect(self, nums1, nums2):
        nums1.sort()
        nums2.sort()
        ans=[]
        for i in nums2:
            if i in nums1:
                ans.append(i)
                nums1.remove(i)
        return ans





print(Solution().intersect([1,2,2,1],[2,2,3]))