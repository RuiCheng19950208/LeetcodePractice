# class Solution(object):
#     def getImportance(self, employees, id):
#
#         def imp(n):
#             ans = n[1]
#             if n[2]!=[]:
#
#                 for i in n[2]:
#                     for j in employees:
#                         if j[0]==i:
#                             ans=ans+imp(j)
#                 return ans
#
#
#
#             else: return ans
#
#         for i in employees[:]:
#             if i[0]==id:
#                 return imp(i)




#标准答案在本地不可运行
class Employee(object):

    def __init__(self, id, importance, subordinates):

        # It's the unique id of each node.

        # unique id of this employee

        self.id = id

        # the importance value of this employee

        self.importance = importance

        # the id of direct subordinates

        self.subordinates = subordinates


class Solution(object):

    def getImportance(self, employees, id):
        emps = {employee.id: employee for employee in employees}

        print(emps)

        def dfs(id):
            subordinates_importance = sum([dfs(sub_id) for sub_id in emps[id].subordinates])

            return subordinates_importance + emps[id].importance

        return dfs(id)



print(Solution().getImportance([[1, 5, [2, 3]], [2, 3, []], [3, 3, []]], 1))