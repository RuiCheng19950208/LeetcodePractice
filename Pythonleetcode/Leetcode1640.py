class Solution(object):
    def canFormArray(self, arr, pieces):
        pieces=sorted(pieces,key = lambda i:len(i),reverse=True)
        check = False
        # print(pieces)
        for i in range(len(pieces)):
            for j in range(len(arr)-len(pieces[i])+1):
                # print(pieces[i],arr[j:j+len(pieces[i])])
                if pieces[i]==arr[j:j+len(pieces[i])]:
                    check=True
            if check==False:
                return False
            check=False
        return True





print(Solution().canFormArray(arr = [85], pieces = [[85]]))
print(Solution().canFormArray(arr = [15,88], pieces = [[88],[15]]))
print(Solution().canFormArray(arr = [49,18,16], pieces = [[16,18,49]]))
print(Solution().canFormArray(arr = [91,4,64,78], pieces = [[78],[4,64],[91]]))
print(Solution().canFormArray(arr = [1,3,5,7], pieces = [[2,4,6,8]]))