class Solution(object):
    def sumOddLengthSubarrays(self, arr):
        max_len=len(arr)
        step=2
        temp_len=1
        ans=0
        if max_len==0:
            return 0
        else:
            while temp_len<=max_len:
                for i in range(max_len-temp_len+1):
                    ans+=sum(arr[i:i+temp_len])
                temp_len+=step
        return ans

print(Solution().sumOddLengthSubarrays([1,4,2,5,3]))
print(Solution().sumOddLengthSubarrays([1,2]))