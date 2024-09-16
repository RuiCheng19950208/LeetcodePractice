class Solution(object):
    def combinationSum(self, candidates, target):
        ans=[]
        sub=[]
        def back(sub, candidates,target,ans):
            for i in candidates:
                if sum(sub)+i<=target and ( sub==[] or i>=max(sub) ):
                    sub.append(i)
                    if sum(sub)==target:
                        ans.append(sub[:])


                    back(sub, candidates, target,ans)
                    sub.remove(i)



        back(sub,candidates,target,ans)
        return ans


print(Solution().combinationSum([2,3,6,7],7))