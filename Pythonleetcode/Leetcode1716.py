class Solution(object):
    def totalMoney(self, n):
        money_list=[1,2,3,4,5,6,7]
        ans=0
        money_list_index = 0
        while n!=0:
            ans += money_list[money_list_index]
            if money_list_index<6:

                money_list_index += 1
            else:
                money_list_index=0
                money_list =[i+1 for i in money_list]
            n-=1
        return ans

print(Solution().totalMoney(4))
print(Solution().totalMoney(10))
print(Solution().totalMoney(20))