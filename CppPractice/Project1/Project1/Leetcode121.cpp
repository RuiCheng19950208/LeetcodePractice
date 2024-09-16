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
    int maxProfit(vector<int>& prices) {
        if (prices.size()<=1)
        {
            return 0;

        }
        int ans = 0;
        int temp_min = prices[i]];
        for (int i = 1; i < prices.size(); i++)
        {
            if (prices[i] <temp_min)
            {
                temp_min = prices[i];

            }
            ans = max(ans, prices[i] - temp_min);

        }

            
        return ans;
    }
};