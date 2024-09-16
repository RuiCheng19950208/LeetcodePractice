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
        int ans = 0;
        int tem_min = prices[0];
        for (int i = 0; i < prices.size(); i++)
        {
            if (prices[i]>prices[i-1])
            {
                ans += prices[i] - prices[i - 1];
            }
        }
        return ans;
    }
};