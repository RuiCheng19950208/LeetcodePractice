class Solution(object):
    def containsNearbyDuplicate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: bool
        """
        index_dict=dict()
        for index,value in enumerate(nums):
            if value in index_dict and index-index_dict[value]<=k:
                return True
            index_dict[value]=index

        return  False






print(Solution().containsNearbyDuplicate(nums = [1,2,3,1], k = 3))
print(Solution().containsNearbyDuplicate(nums = [1,0,1,1], k = 1))
print(Solution().containsNearbyDuplicate(nums = [1,2,3,1,2,3], k = 2))
print(Solution().containsNearbyDuplicate(nums = [99,99], k = 2))
