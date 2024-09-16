class Solution(object):
    def minOperations(self, logs):
        ans=0
        for i in logs:
            if i=="../" and ans>0:
                ans-=1
            elif i=="./":
                pass
            elif i!="../":
                ans+=1


        return ans

print(Solution().minOperations(logs = ["./","../","./"]))

# print(Solution().minOperations(logs = ["d1/","d2/","../","d21/","./"]))
# print(Solution().minOperations(logs = ["d1/","d2/","./","d3/","../","d31/"]))
# print(Solution().minOperations(logs = ["d1/","../","../","../"]))
