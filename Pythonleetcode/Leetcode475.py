class Solution(object):
    def findRadius(self, houses, heaters):
        """
        :type houses: List[int]
        :type heaters: List[int]
        :rtype: int
        """
        houses=sorted(houses)
        heaters=sorted(heaters)
        if len(heaters)==1:
            return max(abs(houses[0]-heaters[0]),abs(houses[-1]-heaters[-1]))
        else:
            ans=0
            heart_1_index=0
            heart_2_index=1

            for i in range(len(houses)):
                while houses[i]>heaters[heart_2_index] and heart_2_index!=len(heaters)-1:
                    heart_1_index += 1
                    heart_2_index += 1
                ans=min(max(ans,abs(houses[i]-heaters[heart_1_index])),max(ans,abs(houses[i]-heaters[heart_2_index])))
                # print(ans,heart_1_index,heart_2_index)
            return ans





print(Solution().findRadius([1,2,3],[2]))
print(Solution().findRadius([1,2,3,4],[1,4]))
print(Solution().findRadius([1],[1,2,3,4]))
print(Solution().findRadius([282475249,622650073,984943658,144108930,470211272,101027544,457850878,458777923],[823564440,115438165,784484492,74243042,114807987,137522503,441282327,16531729,823378840,143542612]))
