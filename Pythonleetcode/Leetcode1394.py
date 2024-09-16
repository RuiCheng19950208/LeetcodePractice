class Solution(object):
    def findLucky(self, arr):
        ans_dict={}
        for i in arr:
             if i not in ans_dict.keys():
                 ans_dict[i]=1
             else:
                 ans_dict[i] += 1
        ans=-1
        for i in sorted(list(ans_dict.keys())):
            if ans_dict[i]==i:
                ans=i
        return ans


print(Solution().findLucky( arr = [2,2,3,4]))
print(Solution().findLucky( arr = [1,2,2,3,3,3]))
print(Solution().findLucky( arr = [2,2,2,3,3]))
print(Solution().findLucky( arr = [5]))