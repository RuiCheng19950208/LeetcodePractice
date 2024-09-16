class Solution(object):
    def maxArea(self, height):
        max_area = 0

        left = 0

        right = len(height) - 1

        while right > left:

            max_area = max(max_area, min(height[left], height[right]) * (right - left))

            if height[right] > height[left]:
                left += 1
            else:
                right -= 1
        return max_area





height=[2,1,3,4,1,5,2]

print(Solution().maxArea(height))