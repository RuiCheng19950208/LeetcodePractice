class Solution(object):
    def findSpecialInteger(self, arr):
        check_length=int(len(arr)/4)
        ans_dir={}
        for i in range(len(arr)):
            if arr[i] not in ans_dir:
                ans_dir[arr[i]]=1
            else:
                ans_dir[arr[i]] += 1
        for i in ans_dir:
            if ans_dir[i]>check_length:
                return i



        return
print(Solution().findSpecialInteger(arr = [1,2,2,6,6,6,6,7,10]))