class Solution(object):
    def uniqueOccurrences(self, arr):
        ans_dict={}
        for key in arr:
            if key not in ans_dict.keys():
                ans_dict[key]=1
            else:
                ans_dict[key] += 1
        value_list=[]
        for i in ans_dict:
            value_list.append(ans_dict[i])
        if len(list(set(value_list)))==len(list(set(arr))):
            return True
        else:
            return False

print(Solution().uniqueOccurrences( [1,2,2,1,1,3]))
print(Solution().uniqueOccurrences( [-3,0,1,-3,1,1,1,-3,10,0]))
print(Solution().uniqueOccurrences( [1,2]))