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
    int missingNumber(vector<int>& nums) {
        sort(nums.begin(),nums.end());
        for (int i = 0; i < nums.size(); i++)
        {
            if (nums[i]!=i)
            {
                return  i;
            }

        }
        return nums.size();

    }
};