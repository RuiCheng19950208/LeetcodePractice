#include <string>

#include <vector>

#include <iostream>

#include <stdlib.h>

#include <time.h>

#include <sstream>

#include <algorithm>

#include <map>

#include <bitset>

#include <set>

using namespace std;

class Solution {
public:
    int findKthLargest(vector<int>& nums, int k) {

        sort(nums.begin(), nums.end());
        for (int i = nums.size(); i > -1; i--)
        {
            k--;
            if (k==0)
            {
                return nums[i];

            }
          

        }
        return;

    }
};