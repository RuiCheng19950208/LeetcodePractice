class Solution(object):
    def checkPossibility(self, nums):



        def dijian(n):
            for i in range(len(n)-1):
                if n[i]>n[i+1]:
                    return False

            return True

        for i in range(len(nums)-1):
            if nums[i]>nums[i+1]:
                print(nums[:i]+nums[i+1:])

                return dijian(nums[:i]+nums[i+1:]) or dijian(nums[:i+1]+nums[i+2:])

        return True




print(Solution().checkPossibility([2,3,3,2,4]))