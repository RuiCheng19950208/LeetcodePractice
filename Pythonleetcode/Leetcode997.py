class Solution(object):
    def findJudge(self, N, trust):
        """
        :type N: int
        :type trust: List[List[int]]
        :rtype: int
        """
        ans=-1
        not_judge=[]

        for i in range(len(trust)):
            if trust[i][0] not in not_judge:
                not_judge.append(trust[i][0])


        for i in range(1,N+1):
            check_pass = 1
            if i not in not_judge:
                for j in range(1,N+1):
                    if j!=i:
                        if [j,i] not in trust:
                            check_pass = 0
                            break
                if check_pass==1:
                    return i


        return ans



print(Solution().findJudge(N = 2, trust = [[1,2]]))
print(Solution().findJudge( N = 3, trust = [[1,3],[2,3]]))
print(Solution().findJudge(N = 3, trust = [[1,3],[2,3],[3,1]]))
print(Solution().findJudge(N = 3, trust = [[1,2],[2,3]]))
print(Solution().findJudge(N = 4, trust = [[1,3],[1,4],[2,3],[2,4],[4,3]]))