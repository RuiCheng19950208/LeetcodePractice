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
    int removeElement(vector<int>& nums, int val) {
        int infi = 10000;
        int ans = nums.size();
        for (int i = 0; i < nums.size(); i++)
        {
            if (nums[i]==val)
            {
                nums[i] = infi;
                ans--;

            }

        }
        sort(nums.begin(), nums.end());
        return ans;



    }
};