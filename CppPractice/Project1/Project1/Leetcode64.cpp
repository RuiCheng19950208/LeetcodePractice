#include <string>

#include <vector>

#include <iostream>

#include <stdlib.h>

#include <time.h>

#include <sstream>

#include <algorithm>

#include <map>

#include <bitset>

using namespace std;

class Solution {
public:
    int minPathSum(vector<vector<int>>& grid) {
        int row = 0;
        int col = 0;
        int g_row = grid.size();
        int g_col = grid[0].size();
        vector<vector<int>> dp(g_row, vector<int>(g_col, 0));
        for (int i = 0; i < g_row; i++)
        {
            if (i==0)
            {
                dp[0][0] = grid[0][0];
            }
            else
            {
                dp[i][0] = grid[i][0]+dp[i-1][0];
            }
        }
        for (int i = 0; i < g_col; i++)
        {
            if (i == 0)
            {
                dp[0][0] = grid[0][0];
            }
            else
            {
                dp[0][i] = grid[0][i] + dp[0][i-1];
            }
        }
        if (g_row==0 or g_col==0)
        {
            return dp[g_row - 1][g_col - 1];
        }
        for (int i = 1; i < g_row; i++)
        {
            for (int j = 1; j < g_col; j++)
            {
                dp[i][j] = min(dp[i - 1][j], dp[i][j - 1]) + grid[i][j];

            }

        }



        return dp[g_row - 1][g_col - 1];

    }
};