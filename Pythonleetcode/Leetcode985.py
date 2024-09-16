class Solution(object):
    def sumEvenAfterQueries(self, A, queries):
        ans=[]
        base=sum([i for i in A if i%2==0])
        for i in queries:

            A[i[1]]+=i[0]
            if A[i[1]]%2==0 and i[0]%2==0:
                base+=i[0]
            elif A[i[1]]%2==1 and i[0]%2==0:
                pass
            elif A[i[1]]%2==0 and i[0]%2==1:
                base += A[i[1]]
            else :
                base += -A[i[1]]+i[0]

            ans.append(base)
            # print(A)
        return ans

print(Solution().sumEvenAfterQueries( A = [1,2,3,4], queries = [[1,0],[-3,1],[-4,0],[2,3]]))
