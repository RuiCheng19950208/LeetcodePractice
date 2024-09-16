class Solution(object):
    def reversePairs(self, nums):
        ans=0
        if len(nums)<2:
            return ans
        dp=[]
        for i in nums:
            dp.append([i])

        left_index=0
        right_index=0
        merge_index=0
        def merge_dp(merge_index,dp):
            left=dp[merge_index]
            right=dp[merge_index+1]
            left.sort()
            right.sort()
            dp[merge_index]=dp[merge_index]+dp[merge_index+1]
            dp.pop(merge_index+1)

            merge_index += 1
            return dp,left,right,merge_index

        while len(dp)>1:
            if merge_index<len(dp)-1:
                dp,left,right,merge_index=merge_dp(merge_index,dp)
            else:
                merge_index=0
                dp, left, right,merge_index = merge_dp(merge_index, dp)
            len_right=len(right)
            len_left=len(left)

            while left_index<len_left and right_index<len_right:
                if left[left_index]>2*right[right_index]:
                    ans+=len_left-left_index
                    right_index+=1
                else:
                    left_index+=1

                if right_index>=len_right:
                    right_index+=1
                    left_index+=1

            left_index=0
            right_index=0
            # print(dp, ans)

        return ans


print(Solution().reversePairs([1,3,2,3,1]))
print(Solution().reversePairs([2,4,3,5,1]))
print(Solution().reversePairs([2147483647,2147483647,-2147483647,-2147483647,-2147483647,2147483647]))


