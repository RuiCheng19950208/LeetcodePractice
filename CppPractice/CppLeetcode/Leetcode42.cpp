#include<vector>
using namespace std;

class Solution {
public:
    int trap(vector<int>& height) 
    {
        int midIndex=0;
        int right=height.size()-1;
        int left=0;
        int ans = 0;
        int heighest = 0;
        for (int i = 0; i < height.size(); i++)
        {
            if(height[i]>heighest)
            {
                heighest = height[i];
                mid = i;
            }
        }
        int tempHeight = height[0];
        while(left<mid)
        {
            if (height[left]<tempHeight)
            {
                ans += tempHeight-height[left];
            }
            else
            {
                tempHeight = height[left];
            }
            left++;
        }
        tempHeight = height.back();
        while(right>mid)
        {
            if (height[right]<tempHeight)
            {
                ans += tempHeight-height[right];
            }
            else
            {
                tempHeight = height[right];
            }
            right--;
        }
        return ans;
    }
};