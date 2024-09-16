
class Solution(object):

    def findRelativeRanks(self, nums):

        sort = sorted(nums)[::-1]

        print(sort)

        rank = ["Gold Medal", "Silver Medal", "Bronze Medal"] + str(range(4, len(nums) + 1))

        print(rank)

        return map(dict(zip(sort, rank)).get, nums)






print(Solution().findRelativeRanks([5, 4, 3, 2, 1]))