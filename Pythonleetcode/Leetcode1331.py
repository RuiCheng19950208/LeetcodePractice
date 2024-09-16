class Solution(object):
    def arrayRankTransform(self, arr):
        ans=[]
        rank_arr=sorted(set(arr))
        ans_dict={}
        rank=1
        for i in rank_arr:
            ans_dict[i]=rank
            rank+=1
        for i in arr:
            ans.append(ans_dict[i])
        return ans


print(Solution().arrayRankTransform(arr = [100,100,100,100]))
print(Solution().arrayRankTransform(arr = [37,12,28,9,100,56,80,5,12]))