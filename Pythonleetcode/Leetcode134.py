class Solution(object):
    def canCompleteCircuit(self, gas, cost):
        def sucess(i,gas,cost):
            total=0
            mark=0
            while (mark!=len(gas)):

                if i<=len(gas)-1:

                    total=total+gas[i]-cost[i]



                    if total<0:
                        return -10
                    mark=mark+1
                    i=i+1
                else:
                    i = 0
                    total = total + gas[i] - cost[i]


                    if total < 0:
                        return -10
                    mark = mark + 1
                    i=1



            return total




        for i in range(len(gas)):
            if sucess(i,gas,cost)>=0:
                return i
        return -1



print(Solution().canCompleteCircuit([1,2,3,4,5], [3,4,5,1,2]))

print(Solution().canCompleteCircuit( [2,3,4], [3,4,3]))

print(Solution().canCompleteCircuit( [3,3,4],[3,4,4]))


