class Solution(object):
    def distributeCandies(self, candies, num_people):
        ans=[0]*num_people
        people_index=0
        candies_need_list=[i+1 for i in range(num_people)]
        while candies>0:


            if candies<candies_need_list[people_index]:
                ans[people_index] +=candies
                candies=0
            else:
                ans[people_index] += candies_need_list[people_index]
                candies -=candies_need_list[people_index]
            if people_index==num_people-1:
                people_index=0
                candies_need_list = [i + num_people for i in candies_need_list]
            else:
                people_index+=1

        return ans

print(Solution().distributeCandies(7,4))
print(Solution().distributeCandies(10,3))

