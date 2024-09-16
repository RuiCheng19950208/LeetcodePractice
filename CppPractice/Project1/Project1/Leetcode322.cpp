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
    int coinChange(vector<int>& coins, int amount) {
        int infinte = 100000;
        vector<int> dp(amount + 1, infinte);
        dp[0] = 0;
        for (int i = 1; i < dp.size(); i++)
        {
            for (int j = 0; j < coins.size(); j++)
            {
                if (i-coins[j]>=0)
                {
                    dp[i] = min(dp[i], dp[i - coins[j]] + 1);
                }
            }
        }
        if (dp.back()== infinte)
        {
            return -1;
        }
        else
        {
            return dp.back();

        }
      

    }
};