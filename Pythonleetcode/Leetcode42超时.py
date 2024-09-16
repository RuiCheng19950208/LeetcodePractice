class Solution(object):
    def trap(self,height):
        height.insert(0,0)
        height.append(0)
        n=0
        for i in range(1,len(height)-1):
            mr=0
            ml=0
            for j in range(0, i):
                for k in range(i+1, len(height)):
                    if height[k]>mr and height[k]>height[i] :
                        mr=height[k]
                    if height[j] > ml  and height[k]>height[i]:
                        ml = height[j]
            # print([ml,mr,height[i]])
            if min(ml,mr)>=height[i]:
                n = n + min(ml, mr) - height[i]

        return n




height=[3,2,1,0,1,2,3]
print(Solution().trap(height))