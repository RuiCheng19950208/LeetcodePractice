class Solution(object):
    def twoSum(self, numbers, target):
        """
        :type numbers: List[int]
        :type target: int
        :rtype: List[int]
        """
        i = 0
        j = len(numbers) - 1
        while True:
            if numbers[i]+numbers[j]>target:
                j -=1
            elif  numbers[i]+numbers[j]<target:
                i +=1
            else:
                return[i+1,j+1]





print(Solution().twoSum(numbers = [2,7,11,15], target = 9))

print(Solution().twoSum(numbers = [2,3,4], target = 6))