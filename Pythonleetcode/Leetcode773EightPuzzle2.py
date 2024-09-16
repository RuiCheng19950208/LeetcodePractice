import collections
import copy

class Solution(object):
    def slidingPuzzle(self, board):
        lenx=len(board)
        leny = len(board[0])
        def board2str(board):
            bstr = []
            for i in range(lenx):
                for j in range(leny):
                    bstr = bstr + [str(board[i][j])]
            return bstr

        goal = []
        for i in range(1,lenx*leny):
            goal=goal+[str(i)]
        goal=goal+['0']
        solution = []
        start = board2str(board)
        bfs = collections.deque()
        bfs.append((start, 0, solution))
        dirs = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        visited = [start]


        while bfs:

            path, step, solution = bfs.popleft()

            if step==20:
                break

            if path == goal:
                return step,solution


            p = path.index('0')
            x, y = int(p / lenx), p % leny
            for dir in dirs:

                tx, ty = x + dir[0], y + dir[1]
                if tx < 0 or tx >= lenx or ty < 0 or ty >= leny:
                    continue
                print('0',visited)
                path[tx * 3 + ty], path[x * 3 + y] = path[x * 3 + y], path[tx * 3 + ty]
                print('1',visited)


                if path not in visited:
                    bfs.append((path, step + 1,solution+[path]))
                    visited.append(path)
                    print(visited)
                path[tx * 3 + ty], path[x * 3 + y] = path[x * 3 + y], path[tx * 3 + ty]
        return -1



# print(Solution().slidingPuzzle([[1,2,3,4],[5,6,7,8],[9,10,11,12],[13,14,0,15]]))
print(Solution().slidingPuzzle([[1,2,3],[4,5,6],[7,0,8]]))

