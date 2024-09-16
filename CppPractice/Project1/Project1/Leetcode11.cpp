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
    int maxArea(vector<int>& height) {
        int ans = 0;
        int left = 0;
        int right = height.size() - 1;
        while (left<right)
        {
            ans = max(ans, (right - left) * min(height[left], height[right]));
            if (height[left]<height[right])
            {
                left++;
            }
            else
            {
                right--;
            }

        }
        return ans;

    }
};