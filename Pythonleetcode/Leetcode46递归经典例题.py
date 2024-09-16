class Solution(object):
    def permute(self, nums):
        def dfs(Nums, subList):

            if len(Nums) == len(subList):
                res.append(subList[:])
            for m in Nums:
                if m in subList:
                    continue
                else:
                    subList.append(m)
                    dfs(Nums, subList)
                    subList.remove(m)

        res=[]
        sub=[]
        dfs(nums,sub)
        return res







print(Solution().permute([1,2,3]))