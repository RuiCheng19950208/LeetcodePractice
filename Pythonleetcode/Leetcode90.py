import copy
class Solution(object):
    def subsetsWithDup(self, nums):
        ans=[]
        ans.append([])
        nums.sort()
        def back(Ans,Nums):
            for i in Nums:
                B=copy.deepcopy(Ans)
                for j in B:
                    j.append(i)
                    if j not in Ans:
                        Ans.append(j)

        back(ans,nums)
        return ans







print(Solution().subsetsWithDup([1,2,3,4]))
print(Solution().subsetsWithDup([1,2,2]))