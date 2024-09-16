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
    int maxProduct(vector<int>& nums) {
        int ans = nums[0];
        int temp_max = nums[0];
        int temp_min = nums[0];
        int temp = 0;
        for (int i = 1; i < nums.size(); i++)
        {
            temp = temp_max;
            temp_max = max({ temp_max * nums[i],temp_min * nums[i],nums[i] });
            temp_min = min({ temp * nums[i],temp_min * nums[i],nums[i] });
            ans = max(ans, temp_max);


        }

        return ans;


    }
};