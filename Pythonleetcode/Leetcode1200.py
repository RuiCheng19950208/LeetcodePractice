class Solution(object):
    def minimumAbsDifference(self, arr):
        """
        :type arr: List[int]
        :rtype: List[List[int]]
        """
        arr=sorted(arr)
        diff=[0]*(len(arr)-1)
        ans=[]
        for i in range(1,len(arr)):
            diff[i-1]=arr[i]-arr[i-1]
        min_diff=min(diff)
        for i in range(len(diff)):
            if diff[i]==min_diff:
                ans.append([arr[i],arr[i+1]])
        return ans





print(Solution().minimumAbsDifference(arr = [4,2,1,3]))
print(Solution().minimumAbsDifference(arr = [1,3,6,10,15]))
print(Solution().minimumAbsDifference(arr = [3,8,-10,23,19,-4,-14,27]))