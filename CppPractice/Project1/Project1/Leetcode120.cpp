
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
    int minimumTotal(vector<vector<int>>& triangle) {
        vector<vector<int>> dp;
        for (int i = 0; i < triangle.size(); i++)
        {
            vector<int> sub(triangle[i].size(), 0);
            dp.push_back(sub);
        }
        if (triangle.size() < 2)
        {
            return triangle[0][0];

        }
        dp[0][0] = triangle[0][0];

        for (int i = 1; i < triangle.size(); i++)
        {
            for (int j = 0; j < triangle[i].size(); j++)
            {
                if (j == 0)
                {
                    dp[i][j] = dp[i - 1][j] + triangle[i][j];

                }
                else if (j == triangle[i].size() - 1)
                {
                    dp[i][j] = dp[i - 1][j - 1] + triangle[i][j];
                }
                else
                {
                    dp[i][j] = min(dp[i - 1][j - 1], dp[i - 1][j]) + triangle[i][j];

                }


            }

        }
        return *min_element(dp.back().begin(), dp.back().end());



    }
};