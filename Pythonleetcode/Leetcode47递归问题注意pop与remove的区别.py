

class Solution(object):
    def permuteUnique(self, nums):
        def dfs(Nums, subList,l):
            if l == len(subList) and subList not in res:
                res.append(subList[:])
            for m in range(len(Nums)):
                subList.append(Nums[m])
                dfs(Nums[:m]+Nums[m+1:], subList,l)
                subList.pop(-1)
        res=[]
        sub=[]
        l=len(nums)
        dfs(nums,sub,l)
        return res


print(Solution().permuteUnique([1,1,2,2]))