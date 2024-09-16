class Solution(object):
    def trap(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        left_ans=0
        right_ans=0
        if len(height)==0:
            return 0

        left_height = height[0]
        right_height = height[-1]
        max_height_index=height.index(max(height))
        for i in range(max_height_index):
            if height[i]>left_height:
                left_height=height[i]
            else:
                left_ans+=(left_height-height[i])


        for i in range(len(height)-1,max_height_index-1,-1):
            if height[i]>right_height:
                right_height=height[i]
            else:
                right_ans+=(right_height-height[i])

        ans=left_ans+right_ans
        return ans




print(Solution().trap(height = [0,1,0,2,1,0,1,3,2,1,2,1]))
print(Solution().trap(height = [4,2,0,3,2,5]))