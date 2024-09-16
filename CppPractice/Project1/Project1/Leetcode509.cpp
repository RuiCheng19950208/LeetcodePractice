#include <string>

#include <vector>

#include <iostream>

#include <stdlib.h>

#include <time.h>

#include <sstream>

#include <algorithm>

#include <map>

using namespace std;


class Solution {
public:
    int fib(int n) {
        vector<int> dp;
        dp.push_back(0);
        dp.push_back(1);
            
        if (n<=1)
        {
            return dp[n];
        }
        for (int i = 2; i < n+1; i++)
        {
            dp.push_back(dp[i - 2] + dp[i - 1]);
        }

        return dp.back();
    }
};