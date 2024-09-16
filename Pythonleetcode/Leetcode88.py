# class Solution(object):
#     def merge(self, nums1, m, nums2, n):
#         k=0
#         for i in range(n):
#             for j in range(m+n):
#                 if nums2[i]<nums1[j]:
#                     nums1=nums1[:j]+[nums2[i]]+nums1[j:]
#                     k=k+1
#                     break
#
#         nums1=nums1[:m+k]+nums2[k:]
#         return nums1



class Solution(object):
    def merge(self, nums1, m, nums2, n):
        n1=nums1[:m]
        n2 = nums2[:n]
        n1=sorted(n1+n2)
        nums1[0:]=n1












print(Solution().merge([1,2,3,4,0,0,0],4, [2,5,6],3))