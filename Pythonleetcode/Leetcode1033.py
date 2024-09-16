class Solution(object):
    def numMovesStones(self, a, b, c):
        """
        :type a: int
        :type b: int
        :type c: int
        :rtype: List[int]
        """
        abs_list=sorted([a,b,c])
        if  abs_list[1]-abs_list[0]==1 and abs_list[2]-abs_list[1]==1:
            return [0,0]
        elif abs_list[1]-abs_list[0]==1 or abs_list[2]-abs_list[1]==1:
            return [1, max(abs_list[1]-abs_list[0],abs_list[2]-abs_list[1])-1]
        elif  abs_list[1]-abs_list[0]==2 or abs_list[2]-abs_list[1]==2:
            return [1, max(abs_list[1] - abs_list[0], abs_list[2] - abs_list[1])]
        else:
            return [2, abs_list[1] - abs_list[0]+abs_list[2] - abs_list[1] - 2]





print(Solution().numMovesStones(a = 1, b = 2, c = 5))
print(Solution().numMovesStones(a = 4, b = 3, c = 2))
print(Solution().numMovesStones( a = 3, b = 5, c = 1))
print(Solution().numMovesStones( a = 1, b = 4, c = 7))
