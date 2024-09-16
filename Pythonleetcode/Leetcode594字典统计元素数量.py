# class Solution(object):
#     def findLHS(self, nums):
#         if nums==[]:
#             return 0
#
#         nums=sorted(nums)
#         nums1=sorted(list(set(nums)))
#         if len(nums1)==1:
#             return 0
#         result=[0]*len(nums1)
#         for i in range(len(nums1)):
#             result[i]=nums.count(nums1[i])
#         max1=0
#         for i in range(1,len(nums1)):
#             if nums1[i]-nums1[i-1]==1 and result[i]+result[i-1]>max1:
#                 max1=result[i]+result[i-1]
#
#         return max1
# 超时



class Solution:

    def findLHS(self, nums):

        dict1 = {}

        x = 0

        b = 0

        for i in range(len(nums)):

            dict1[nums[i]] = dict1.get(nums[i],0) + 1

        for v in dict1:

            if v + 1 in dict1:

                b = dict1[v] + dict1[v+1]

                if b > x:

                    x = b

        return x






print(Solution().findLHS([1,3,2,2,5,2,3,7]))
print(Solution().findLHS([-1,0,-1,0,-1,0,-1]))
print(Solution().findLHS([11,95,33,81,-24,-2,-99,29,84,10,22,77,51,67,27,52,100,73,85,48,81,99,51,88,99,12,-22,77,97,68,-44,59,57,-35,22,2,74,52,25,14,49,40,-76,90,41,72,88,35,-28,77,0,77,-29,66,-43,59,1,52,54,86,98,47,53,80,37,-41,26,28,11,58,38,73,85,83,42,4,6,87,52,23,61,20,30,24,51,-38,-93,-40,-37,40,-57,-31,-72,-67,88,69,2,78,42,80,47,59,48,-53,90,8,8,90,55,85,11,95,10]))