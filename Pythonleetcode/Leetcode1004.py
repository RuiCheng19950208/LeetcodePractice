class Solution(object):
    def longestOnes(self, A, K):
        if K>=len(A):
            return len(A)
        low_point=0
        high_point=K-1
        count_zeros = len(A[:high_point+1])-sum(A[:high_point+1])
        ans=0
        # print(low_point,high_point,count_zeros)
        while high_point<len(A)-1:
            if high_point<len(A)-1:
                high_point+=1
                if A[high_point]==0:
                    count_zeros+=1
            if count_zeros>=K+1:
                if A[low_point]==0:
                    count_zeros-=1
                low_point += 1
            else:
                ans=max(ans,high_point-low_point+1)

            # print(low_point, high_point, count_zeros)

        return ans

print(Solution().longestOnes(A = [1,1,1,0,0,0,1,1,1,1,0], K = 2))
print(Solution().longestOnes( A = [0,0,1,1,0,0,1,1,1,0,1,1,0,0,0,1,1,1,1], K = 3))
