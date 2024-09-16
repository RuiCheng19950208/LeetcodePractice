#include <vector>
using namespace std;
class Solution {
public:
    int longestSubarray(vector<int>& nums) {
        int res=0;
        int temp=0;
        int maxVal = *max_element(nums.begin(),nums.end());
        for(int num : nums)
        {
            if(num==maxVal)
            {
                temp++;
                res=max({temp,res});
            }
            else
            {
                temp=0;
            }
        }
        return res;
    }
};