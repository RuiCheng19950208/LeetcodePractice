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
    vector<int> smallerNumbersThanCurrent(vector<int>& nums) {
        map<int, int> dict;
        vector<int> ans;
        for (int i = 0; i < nums.size(); i++)
        {
            if (dict.find(nums[i]) == dict.end())
            {
                dict[nums[i]] = 0;
            }
            dict[nums[i]] += 1;

        }
        int temp = 0;
        for (int i = 0; i < nums.size(); i++)
        {
            for (auto pair : dict)
            {
                if (nums[i] > pair.first)
                {
                    temp += dict[pair.first];
                }
            }
            ans.push_back(temp);
            temp = 0;
        }
        return ans;

    }
};