class Solution(object):
    def poorPigs(self, buckets, minutesToDie, minutesToTest):
        if buckets == 1:
            return 0
        a = (minutesToTest // minutesToDie) + 1
        b = (minutesToTest // minutesToDie) + 1
        ans = 1

        while b < buckets:
            b = b * a

            ans = ans + 1
        return ans




print(Solution().poorPigs(1000,15,60))