class Solution(object):
    def frequencySort(self, nums):
        ans_dict={}
        nums=sorted(nums)[::-1]
        for i in nums:
            if i not in ans_dict.keys():
                ans_dict[i] =1
            else:
                ans_dict[i] +=1
        value_list=[]
        for i in ans_dict:
            value_list.append(ans_dict[i])
        sort_value_list=sorted(value_list)
        ans=[]
        for i in sorted(list(set(sort_value_list))):
            for key in sorted(list(ans_dict))[::-1]:
                if ans_dict[key]==i:
                    for j in range(i):
                        ans.append(key)
        return ans


print(Solution().frequencySort( [1,1,2,2,2,3]))
print(Solution().frequencySort([-39,27,27,-11,-39,-11,-11,27,-11,-26,-33,-26,-11,0,-11,0,-26,27,-39,-26,0,27,-33,-33,27,0,27,27,-33,0,-11,-26,-11]))
print(Solution().frequencySort( [-1,1,-6,4,5,-6,1,4,1]))