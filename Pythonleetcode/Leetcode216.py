class Solution(object):
    def combinationSum3(self, k, n):
        sub=[]
        ans=[]
        def back(sub,k,n,ans):
            for i in range(1,10):

                if sum(sub)+i<=n and (sub==[] or i>=max(sub)) and (i not in sub):
                    sub.append(i)
                    if sum(sub)==n and k==1:
                        ans.append(sub[:])
                    back(sub,k-1,n,ans)
                    sub.remove(i)





        back(sub,k,n,ans)
        return ans





print(Solution().combinationSum3(3, 7))