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
    int majorityElement(vector<int>& nums) {
        map<int, int> dict;
        int count=0;
        int ans;

        for (int i = 0; i < nums.size(); i++)
        {
            dict[nums[i]]++;
        }
        for (auto x:dict)
        {
            if (x.second>count)
            {
                count = x.second;
                ans = x.first;
            }
        }
        return ans;

    }
};