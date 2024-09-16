#include "LeetcodeHeader.h"

class Solution {
public:
    int trap(vector<int>& height) {
        int anchor=0;
        int temp_max = 0;
        int ans = 0;
        if (height.size()<3)
        {
            return 0;
        }
        for (int i = 0; i < height.size(); i++)
        {
            if (height[i]>height[anchor])
            {
                anchor = i;
            }

        }

        for (int i = 0; i < anchor; i++)
        {
            if (height[i]>temp_max)
            {
                temp_max = height[i];

            }
            else
            {
                ans += temp_max-height[i];

            }
        }

        temp_max = 0;
        for (int i = height.size()-1; i > anchor ; i--)
        {
            if (height[i] > temp_max)
            {
                temp_max = height[i];

            }
            else
            {
                ans += temp_max - height[i];

            }

        }
        return ans;

    }
};