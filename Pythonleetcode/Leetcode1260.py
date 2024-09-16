class Solution(object):
    def shiftGrid(self, grid, k):
        grid_list=[]
        for i in grid:
            grid_list+=i
        k=k%len(grid_list)
        shift_list=grid_list[-k:]+grid_list[:-k]
        ans=[]
        col=len(grid[0])
        for i in range(len(grid)):
            ans.append(shift_list[i*col:(i+1)*col])
        return ans

print(Solution().shiftGrid(grid = [[1,2,3],[4,5,6],[7,8,9]], k = 1))
print(Solution().shiftGrid(grid = [[3,8,1,9],[19,7,2,5],[4,6,11,10],[12,0,21,13]], k = 4))
print(Solution().shiftGrid(grid = [[1,2,3],[4,5,6],[7,8,9]], k = 9))