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
    int numSquares(int n) {
        vector<int> dp(n + 1, INT_MAX);
        dp[0] = 0;
        for (int i = 1; i <= sqrt(n); i++)
        {
            dp[i * i] = 1;

        }
        for (int i = 0; i < n+1; i++)
        {
            for (int j = 1; j <= sqrt(i); j++)
            {
                dp[i] = min(dp[i], dp[i - j * j]+1);

            }

        }

        

        return dp.back();

    }
};