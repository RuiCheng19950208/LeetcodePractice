# #实际上和参考答案思路一致，但是超时
# class Solution(object):
#     def findDiagonalOrder(self, nums):
#         ans=[]
#         ans_dict={}
#         for i in range(len(nums)):
#             for n in range(len(nums[i])):
#                 if n+i not in ans_dict.keys():
#                     ans_dict[i+n]=[nums[i][n]]
#                 else:
#                     ans_dict[i + n].insert(0, nums[i][n])
#         for i in ans_dict:
#                 ans+=ans_dict[i]
#         return ans


#在上面的基础上改换一句话即可通过且快于90%（ans_dict=defaultdict(list)，定义dict为list，你妈的，玩我呢？）
# class Solution(object):
#     def findDiagonalOrder(self, nums):
#         ans=[]
#         ans_dict=defaultdict(list)
#         for i in range(len(nums)):
#             for n in range(len(nums[i])):
#                 ans_dict[i + n].insert(0, nums[i][n])
#         for i in ans_dict:
#                 ans+=ans_dict[i]
#         return ans



# class Solution(object):
#     def findDiagonalOrder(self, nums):
#         diagonal_dict = defaultdict(list)
#         for i in range(len(nums)):
#             idx = 0
#             for num in nums[i]:
#                 diagonal_dict[i + idx].append(num)
#                 idx += 1
#         result = []
#         for i in range(len(diagonal_dict)):
#             result += diagonal_dict[i][::-1]
#         return result



print(Solution().findDiagonalOrder(nums = [[1,2,3],[4,5,6],[7,8,9]]))
print(Solution().findDiagonalOrder(nums = [[1,2,3,4,5],[6,7],[8],[9,10,11],[12,13,14,15,16]]))
print(Solution().findDiagonalOrder( nums = [[1,2,3],[4],[5,6,7],[8],[9,10,11]]))
print(Solution().findDiagonalOrder(nums = [[1,2,3,4,5,6]]))