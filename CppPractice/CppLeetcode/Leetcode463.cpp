#include<vector>

class Solution {
    
public:
    int ans=0;
    int islandPerimeter(vector<vector<int>> &grid) {
        for (int i = 0; i < grid.size(); i++)
        {
            for (int j = 0; j < grid[0].size(); j++)
            {
                if (grid[i][j]==1)
                {
                    if (i==0 || grid[i-1][j]==0)
                    {
                        ans++;
                    }
                    if (i==grid.size()-1 || grid[i+1][j]==0)
                    {
                        ans++;
                    }
                    if (j==0 || grid[i][j-1]==0)
                    {
                        ans++;
                    }
                    if (j==grid[0].size()-1 || grid[i][j+1]==0)
                    {
                        ans++;
                    }
                }
            }
        }
        return ans;
    }
};