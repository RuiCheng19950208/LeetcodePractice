class Solution(object):
    def numberOfSubarrays(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        def temp_C(l,r,len_nums,odd_index_list):
            if l==0 and r==len(odd_index_list)-1:

                right_chice =len_nums-odd_index_list[r]
                left_choice =1+odd_index_list[l]

            elif l==0:
                right_chice = odd_index_list[r+1]-odd_index_list[r]
                left_choice = 1+odd_index_list[l]

            elif r==len(odd_index_list)-1:
                right_chice =len_nums-odd_index_list[r]
                left_choice =odd_index_list[l]-odd_index_list[l-1]

            else:
                right_chice = odd_index_list[r+1]-odd_index_list[r]
                left_choice = odd_index_list[l]-odd_index_list[l-1]

            return left_choice*right_chice


        odd_index_list=[]
        for i in range(len(nums)):
            nums[i]=nums[i]%2
            if nums[i]==1:
                odd_index_list.append(i)
        if len(odd_index_list)<k:
            return 0
        else:
            ans=0
            l=0
            r=k-1
            len_num=len(nums)
            while r<len(odd_index_list):
                ans+=temp_C(l,r,len_num,odd_index_list)
                l+=1
                r+=1
        return ans

print(Solution().numberOfSubarrays( nums = [1,1,2,1,1], k = 3))
print(Solution().numberOfSubarrays( nums = [2,4,6], k = 1))
print(Solution().numberOfSubarrays( nums = [2,2,2,1,2,2,1,2,2,2], k = 2))