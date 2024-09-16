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
    int singleNumber(vector<int>& nums) {
        sort(nums.begin(), nums.end());
        if (nums.size()==1)
        {
            return nums[0];
        }
        for (int i = 1; i < nums.size()-1; i++)
        {
            if (nums[i]!=nums[i-1] and nums[i]!=nums[i+1])
            {
                return nums[i];
            }
        }
        if (nums[0]==nums[1])
        {
            return nums[nums.size() - 1];
        }
        else
        {
            return nums[0];
        }
    }
};