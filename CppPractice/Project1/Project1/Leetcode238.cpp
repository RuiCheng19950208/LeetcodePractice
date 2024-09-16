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
    vector<int> productExceptSelf(vector<int>& nums) {
        int product = 1;
        int zero_count = 0;
        int product_no_zero = 1;
        vector<int> ans;
        for (int i = 0; i < nums.size(); i++)
        {
            if (nums[i]==0 and zero_count<1)
            {
                product *= nums[i];
                zero_count += 1;

            }
            else
            {
                product *= nums[i];
                product_no_zero *= nums[i];

            }
        }
        for (int i = 0; i < nums.size(); i++)
        {
            if (nums[i]==0)
            {
                ans.push_back(product_no_zero);
            }
            else
            {
                ans.push_back(product / nums[i]);
            }
           

        }
        return ans;

    }
};