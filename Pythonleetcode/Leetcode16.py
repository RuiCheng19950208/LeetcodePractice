class Solution(object):
    def threeSumClosest(self, nums, target):
        nums.sort()
        # print(nums)
        dif = float('inf')
        for i in range(len(nums)-2):
            lo = i+1
            hi = len(nums)-1
            while lo<hi:
                SumThree=nums[i]+nums[lo]+nums[hi]
                if SumThree-target==0:
                    return target
                if abs(SumThree-target)<abs(dif):
                    dif = SumThree-target
                # print([i, lo, hi], SumThree, dif)
                if SumThree-target<0:
                    lo +=1
                else:
                    hi-=1

        return dif+target


print(Solution().threeSumClosest([-1,2,1,-4], 1))
print(Solution().threeSumClosest([0,0,0], 1))

