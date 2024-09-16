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
    int change(int amount, vector<int>& coins) {
        vector<vector<int>> dp(coins.size()+1, vector<int>(amount + 1,0));
        for (int i = 0; i < coins.size()+1; i++)
        {
            dp[i][0] = 1;
        }
        for (int i = 1; i < dp.size(); i++)
        {
            for (int j = 1; j < dp[0].size(); j++)
            {
                if (j-coins[i-1]>=0)
                {
                    dp[i][j]= dp[i - 1][j]+dp[i][j-coins[i-1]];
                }
                else
                {
                    dp[i][j] = dp[i - 1][j];
                }

            }

        }


        return dp.back().back();

    }
};