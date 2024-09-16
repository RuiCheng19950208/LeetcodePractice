#include <vector>
#include <set>
using namespace std;

class Solution {
public:
    vector<vector<int>> threeSum(vector<int>& nums) 
    {
        vector<vector<int>>  ans;
        int lenN = nums.size();
        sort(nums.begin(), nums.end());
        for(int i = 0; i < lenN; i++)
        {
            if(i>0 && nums[i]==nums[i-1])
            {
                continue;
            }
            int left = i+1;
            int right=lenN-1;
            while (left<right)
            {
                int theSum =nums[i]+nums[left]+nums[right];
                if(theSum==0)
                {
                    ans.push_back({nums[i],nums[left],nums[right]});
                    left++;
                    right--;
                    while (left<right && nums[left]==nums[left-1])
                    {
                        left++;
                    }
                    while (left<right && nums[right]==nums[right-1])
                    {
                        right--;
                    }
                }
                else if (theSum<0)
                {
                    left++;
                    while (left<right && nums[left]==nums[left-1])
                    {
                        left++;
                    }
                }
                else
                {
                    right--;
                    while (left<right && nums[right]==nums[right-1])
                    {
                        right--;
                    }
                }
            }   
        }
        return ans;
    }
}