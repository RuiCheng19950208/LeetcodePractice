class Solution(object):
    def kConcatenationMaxSum(self, arr, k):
        def find_sub_max(arr):
            sum_arr=sum(arr)
            l = 0
            r = len(arr) - 1
            temp_sum=sum_arr-arr[0]-arr[-1]
            temp = max(0,temp_sum)
            while l<=r-1:
                print(l,r)
                if arr[l+1]<=arr[r-1]:
                    l+=1
                    temp_sum-=arr[l]
                    temp=max(temp,temp_sum)
                else:
                    r -= 1
                    temp_sum -= arr[r]
                    temp = max(temp, temp_sum)
            return max(temp,sum_arr-arr[-1],sum_arr-arr[0],sum_arr)

        if len(arr)==1:
            if arr[0]>=0:
                return k*arr[0]
            else:
                return 0
        if k==1:
            max_val=find_sub_max(arr)
            return max_val
        else:
            arr_concat=arr+arr
            max_val = find_sub_max(arr_concat)
        sum_arr=sum(arr)

        print(max_val,sum_arr)
        if 2*sum_arr==max_val:
            return k*sum_arr
        elif sum_arr>0:
            return max_val+(k-2)*sum_arr
        elif sum_arr<=0:
            return max_val



# print(Solution().kConcatenationMaxSum( arr = [1,2], k = 3))
# print(Solution().kConcatenationMaxSum( arr = [1,-2,1], k = 5))
# print(Solution().kConcatenationMaxSum( arr = [-1,-2], k = 7))
# print(Solution().kConcatenationMaxSum( arr = [-1,1], k = 7))
# print(Solution().kConcatenationMaxSum( arr = [-5,4,-4,-3,5,-3], k = 3))
print(Solution().kConcatenationMaxSum( arr = [-7,-1,5,2,3,-7,-6,1], k = 6))
print(Solution().kConcatenationMaxSum( arr =[-1,5,-7,2,-1,0,7,6,2,4], k = 5))


