class Solution(object):
    def mostVisited(self, n, rounds):
        # mark=rounds[0]
        # round_num=0
        # temp_min=rounds[0]
        # for i in rounds:
        #     if i<=temp_min:
        #         temp_min=i
        #         round_num+=1
        # print(temp_min,round_num)
        if rounds[0]<=rounds[-1]:
            return [i for i in range(rounds[0],rounds[-1]+1)]
        else:
            return [i for i in range(1,rounds[-1]+1)]+[i for i in range(rounds[0],n+1)]



print(Solution().mostVisited(n = 4, rounds = [1,3,1,2]))
print(Solution().mostVisited(n = 2, rounds = [2,1,2,1,2,1,2,1,2]))
print(Solution().mostVisited(n = 7, rounds = [1,3,5,7]))