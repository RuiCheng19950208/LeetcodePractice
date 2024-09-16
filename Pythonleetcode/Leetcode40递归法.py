class Solution(object):
    def combinationSum2(self, candidates, target):
        ans=[]
        sub=[]
        def back(sub, candidates,target,ans):
            for i in range(len(candidates)):
                if sum(sub)+candidates[i]<=target and ( sub==[] or candidates[i]>=max(sub) ):
                    sub.append(candidates[i])
                    if sum(sub)==target and sub not in ans:
                        ans.append(sub[:])


                    back(sub, candidates[:i]+candidates[i+1:], target,ans)
                    sub.pop(-1)



        back(sub,candidates,target,ans)
        return ans


print(Solution().combinationSum2( [2,2,3,5],7))