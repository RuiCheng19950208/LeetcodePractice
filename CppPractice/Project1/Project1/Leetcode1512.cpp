#include <string>

#include <vector>

#include <iostream>

#include <stdlib.h>

#include <time.h>

#include <sstream>

#include <algorithm>

#include <map>

using namespace std;


// first solution is double for loop


class Solution {
public:
    int numIdenticalPairs(vector<int>& nums) {
        int ans=0;
        for (size_t i = 0; i < nums.size()-1; i++)
        {
            for (int j = i+1;  j< nums.size(); j++)
            {
                if (nums[j]==nums[i])
                {
                    ans += 1;
                }
            }
        }
        return ans;
    }
};


// second solution based on map


class Solution {
public:
    int numIdenticalPairs(vector<int>& nums) {
        map<int, int> intKey;
        int res = 0;
        for (int each : nums)
        {
            if (intKey.find(each) == intKey.end())
            {
                intKey[each] = 0;
            }
            intKey[each] += 1;
            res += (intKey[each] - 1);
        }
        return res;
    }

};

