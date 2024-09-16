class Solution(object):
    def canVisitAllRooms(self, rooms):
        target=[]
        reach=[0]
        for i in range(len(rooms)):
            target.append(i)

        def collect(s):
            for i in s:
                if i not in reach:
                        reach.append(i)
                else: continue
                collect(rooms[i])


        collect(rooms[0])
        if sorted(reach)!=target:
            return False
        else:
            return True








print(Solution().canVisitAllRooms([[1],[2],[3],[]]))
print(Solution().canVisitAllRooms([[1,3],[3,0,1],[2],[0]]))