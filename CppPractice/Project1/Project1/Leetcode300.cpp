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
    int lengthOfLIS(vector<int>& nums) {
        vector<int> dp(nums.size(), 1);
        for (int i = 1; i < nums.size(); i++)
        {
            for (int j = i - 1; j > -1; j--)
            {
                if (nums[j] < nums[i])
                {
                    dp[i] = max(dp[i], dp[j] + 1);

                }

            }
            cout << dp[i];
        }
        return *max_element(dp.begin(),dp.end());


    }
};