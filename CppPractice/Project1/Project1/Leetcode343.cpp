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
    int integerBreak(int n) {
        vector<int> dp(n + 1, 1);
        int temp = 0;
        for (int i = 2; i <= n; i++)
        {
            for (int j =1; j < i; j++)
            {
                temp = max(temp,j*dp[i-j]);
                temp = max(temp,j*(i-j));
            }
            dp[i] = temp;
            temp = 0;
        }
        return dp[n];

    }
};
