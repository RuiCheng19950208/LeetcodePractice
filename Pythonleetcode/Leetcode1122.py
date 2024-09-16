class Solution(object):
    def relativeSortArray(self, arr1, arr2):
        arr1=sorted(arr1)
        ans_dict={}
        for i in arr1:
            if i not in ans_dict.keys():
                ans_dict[i]=1
            else:
                ans_dict[i] += 1
        # print(ans_dict)
        ans_list=[]
        for i in arr2:
            for j in range(ans_dict[i]):
                ans_list.append(i)
            del ans_dict[i]
        for i in sorted(list(ans_dict.keys())):
            for j in range(ans_dict[i]):
                ans_list.append(i)
        return ans_list
print(Solution().relativeSortArray(arr1 = [2,3,1,3,2,4,6,7,9,2,19], arr2 = [2,1,4,3,9,6]))
print(Solution().relativeSortArray([28,6,22,8,44,17],[22,28,8,6]))
