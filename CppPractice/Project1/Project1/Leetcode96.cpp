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
    int numTrees(int n) {
        int ans = 0;
        vector<int> dp(n + 1, 0);

        for (int i = 0; i < n + 1; i++)
        {
            if (i < 2)
            {
                dp[i] = 1;

            }
            else
            {
                for (int j = 0; j < i; j++)
                {
                    dp[i] += dp[j] * dp[i - j - 1];

                }
            }
        }

        return dp.back();

    }


};