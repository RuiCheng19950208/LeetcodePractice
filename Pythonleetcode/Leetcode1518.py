class Solution(object):
    def numWaterBottles(self, numBottles, numExchange):
        ans=numBottles
        bottles = numBottles
        exchange=bottles // numExchange
        bottles=bottles%numExchange+exchange

        ans+=exchange


        while exchange>0:
            exchange = bottles // numExchange
            bottles = bottles % numExchange + exchange
            ans += exchange


        return ans


print(Solution().numWaterBottles(numBottles = 9, numExchange = 3))
print(Solution().numWaterBottles(numBottles = 15, numExchange = 4))