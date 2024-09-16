class Solution(object):
    def findRestaurant(self, list1, list2):
        """
        :type list1: List[str]
        :type list2: List[str]
        :rtype: List[str]
        """
        ans=[]

        common=[i for i in list1 if i in list2]
        index_sum=10**10
        for i in range(len(common)):
            if list1.index(common[i])+list2.index(common[i])<index_sum:
                ans=[]
                ans.append(common[i])
                index_sum = list1.index(common[i]) + list2.index(common[i])
            elif list1.index(common[i])+list2.index(common[i])==index_sum:
                ans.append(common[i])
        return ans



print(Solution().findRestaurant(["Shogun", "Tapioca Express", "Burger King", "KFC"]
,["Piatti", "The Grill at Torrey Pines", "Hungry Hunter Steakhouse", "Shogun"]))


print(Solution().findRestaurant(["Shogun", "Tapioca Express", "Burger King", "KFC"]
,["KFC", "Shogun", "Burger King"]))

print(Solution().findRestaurant(["Shogun","Tapioca Express","Burger King","KFC"],
["KFC","Burger King","Tapioca Express","Shogun"]))
