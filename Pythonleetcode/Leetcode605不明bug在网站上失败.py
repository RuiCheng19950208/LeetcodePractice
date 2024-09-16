class Solution(object):
    def canPlaceFlowers(self, flowerbed, n):
        start=-1
        end=-1
        result=0

        for i in range(len(flowerbed)):

            if flowerbed[i]==1:
                end=i
                if end-start!=0:
                    result=result+int((end-start-2)/2)
                start=i

        return result>=n



print(Solution().canPlaceFlowers([1,0,0,0,1], 1))
print(Solution().canPlaceFlowers([1,0,0,0,0,1], 1))
print(Solution().canPlaceFlowers([1,0,0,0,0,0,1], 1))

print(Solution().canPlaceFlowers([1,0,0,0,1],1))
print(Solution().canPlaceFlowers([0,0,0,0,0],3))

