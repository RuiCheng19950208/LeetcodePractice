
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
    int climbStairs(int n) {

        if (n == 1)
        {
            return 1;

        }
        vector<int> dp(n + 1, 1);
        for (int i = 2; i < n+1; i++)
        {
            dp[i] = dp[i - 1] + dp[i - 2];

        }

        return dp.back();

    }
};