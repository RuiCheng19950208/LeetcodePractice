class Solution(object):
    def findKthPositive(self, arr, k):
        for i in range(len(arr)):
            if arr[i]-i-1>=k:
                ans=i+k
                return ans

        return len(arr)+k

print(Solution().findKthPositive(arr = [2,3,4,7,11], k = 5))
print(Solution().findKthPositive([5,6,7,8,9],9))