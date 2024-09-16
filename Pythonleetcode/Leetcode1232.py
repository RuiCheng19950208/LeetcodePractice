class Solution(object):
    def checkStraightLine(self, coordinates):
        """
        :type coordinates: List[List[int]]
        :rtype: bool
        """
        sorted(coordinates)
        index=2
        x_cha=coordinates[1][0]-coordinates[0][0]
        y_cha=coordinates[1][1]-coordinates[0][1]
        if x_cha==0:
            while index < len(coordinates):
                if coordinates[index][0] - coordinates[index - 1][0] != 0:
                    return False
                index += 1
            return True

        elif y_cha==0:
            while index < len(coordinates):
                if coordinates[index][1] - coordinates[index - 1][1] != 0:
                    return False
                index += 1
            return True
        else:
            slope=y_cha/x_cha
            while index<len(coordinates):
                if (coordinates[index][0]-coordinates[index-1][0])==0 or (coordinates[index][1]-coordinates[index-1][1])/(coordinates[index][0]-coordinates[index-1][0])!=slope:
                    return False
                index +=1
            return True



print(Solution().checkStraightLine( coordinates = [[1,2],[2,3],[3,4],[4,5],[5,6],[6,7]]))
print(Solution().checkStraightLine( coordinates = [[1,1],[2,2],[3,4],[4,5],[5,6],[7,7]]))
print(Solution().checkStraightLine( coordinates = [[0,0],[0,1],[0,-1]]))
