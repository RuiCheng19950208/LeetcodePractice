class Solution(object):
    def trimMean(self, arr):
        remove_length=int(0.05*len(arr))
        arr=sorted(arr)
        ans=0
        for i in arr[remove_length:len(arr)-remove_length]:
            ans+=float(i)
        return ans/(len(arr)-2*remove_length)

print(Solution().trimMean([1,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,3]))
print(Solution().trimMean([6,2,7,5,1,2,0,3,10,2,5,0,5,5,0,8,7,6,8,0]))
print(Solution().trimMean([6,0,7,0,7,5,7,8,3,4,0,7,8,1,6,8,1,1,2,4,8,1,9,5,4,3,8,5,10,8,6,6,1,0,6,10,8,2,3,4]))