# class Solution(object):
#     def canReach(self, arr, start):
#         """
#         :type arr: List[int]
#         :type start: int
#         :rtype: bool
#         """
#         zero_index=[]
#         for i in range(len(arr)):
#             if arr[i]==0:
#                 zero_index.append(i)
#         can_reach=[False]*len(zero_index)
#
#         if len(zero_index)==0:
#             return False
#
#         for i in range(len(zero_index)):
#             considered=[False]*len(arr)
#             present_index=[start]
#             while len(present_index)>0:
#                 tem=[]
#                 break_bol=0
#                 for j in present_index:
#                     if j + arr[j]<len(arr) and considered[ j + arr[j]]==False:
#                         tem.append( j + arr[j])
#                     if j - arr[j]>=0 and considered[j - arr[j]]==False:
#                         tem.append(j - arr[j])
#                     considered[j] = True
#                     if zero_index[i]==j + arr[j] or zero_index[i]==j - arr[j]:
#                         can_reach[i] =True
#                         break_bol=1
#                         break
#                 present_index = tem
#                 if break_bol==1:
#                     break
#
#         # print(can_reach)
#         return any(can_reach)

class Solution(object):
    def canReach(self, arr, start):
        if 0 <= start < len(arr) and arr[start] >= 0:
            if arr[start] == 0:
                return True
            arr[start] = -arr[start]
            return self.canReach(arr, start+arr[start]) or self.canReach(arr, start-arr[start])
        return False

print(Solution().canReach(arr = [4,2,3,0,3,1,2], start = 5))
print(Solution().canReach(arr = [4,2,3,0,3,1,2], start = 0))
print(Solution().canReach(arr = [3,0,2,1,2], start = 2))
print(Solution().canReach(arr = [0,3,0,6,3,3,4], start = 6))

