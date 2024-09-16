#include<vector>
#include <iostream>
#include <ostream>
using namespace std;

class Solution {
private:
    void bfs(int i,int j, vector<vector<char>> &grid)
    {
        if (i<0||j<0||i>=grid.size() || j>=grid[0].size()||grid[i][j]=='0')
        {
            return;
        }
        else
        {
            grid[i][j]='0';
            bfs(i,j+1,grid);
            bfs(i,j-1,grid);
            bfs(i+1,j,grid);
            bfs(i-1,j,grid);
        }
        
        return;
    }
public:
    int numIslands(vector<vector<char>> &grid) 
    {
        int ans=0;
        for (int i = 0; i < grid.size(); i++)
        {
            for (int j = 0; j < grid[0].size(); j++)
            {
                if (grid[i][j]=='1')
                {
                    ans++;
                    bfs(i,j,grid);
                }
            }
        }
        return ans;
    }
};

// int main () {
//     Solution solution;
//     vector<vector<char>> grid = {
//         {'1', '1', '0', '0', '0'},
//         {'1', '1', '0', '0', '0'},
//         {'0', '0', '1', '0', '0'},
//         {'0', '0', '0', '1', '1'}
//     };
//     int result = solution.numIslands(grid);
//     cout << "Number of islands: " << result << endl;
//     return 0;
// }