# import copy
# class Solution(object):
#     def subsets(self, nums):
#         ans=[]
#         self.k=copy.deepcopy(nums)
#
#
#
#         self.back(ans, nums)
#         return ans
#
#     def back(self,Ans,Nums):
#         if not Nums in Ans:
#             Ans.append(Nums[:])
#
#         for i in Nums:
#             print(i)
#             Nums.remove(i)
#             self.back(Ans, Nums)
#             self.Nums=self.k
#             print(self.Nums)
#             print(i)




class Solution(object):

    def subsets(self, nums):

        res=[[]]

        for i in nums:
            for k in res[:]:
                x=k[:]
                x.append(i)
                res.append(x)

        return res

print(Solution().subsets([1,2,3]))