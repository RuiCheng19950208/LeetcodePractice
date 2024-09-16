class Solution(object):
    def isPathCrossing(self, path):
        direct_dict={"N":[0,1],"S":[0,-1],"E":[1,0],"W":[-1,0]}
        walked=[[0,0]]
        curr_loc=[0,0]
        for i in path:
            curr_loc=[curr_loc[0]+direct_dict[i][0],curr_loc[1]+direct_dict[i][1]]

            if curr_loc in walked:
                return True
            walked.append(curr_loc)
        return False

print(Solution().isPathCrossing(path = "NES"))
print(Solution().isPathCrossing(path = "NESWW"))