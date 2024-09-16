#include <vector>
#include <set>
using namespace std;

class Solution {
public:
    vector<vector<int>> threeSum(vector<int>& nums) 
    {
        vector<vector<int>> res;
        set<int> visitedAnchor;
        int anchor;
        int lenN  = nums.size();
        // Sort the vector in ascending order
        sort(nums.begin(), nums.end());
        for(int i = 0; i < nums.size(); i++)
        {
            anchor = nums[i];
            if(visitedAnchor.find(anchor) == visitedAnchor.end())
            {
                int left = i+1;
                int right = lenN-1;
                while (left<right)
                {
                    vector<int> temp = {anchor,nums[left],nums[right]};
                    int theSum  = accumulate(temp.begin(), temp.end(), 0);
                    if(theSum==0)
                    {
                        res.push_back(temp);
                        left++;
                        while (left<right &&nums[left]==nums[left-1])
                        {
                            left++;
                        }
                        
                    }
                    else if (theSum<0)
                    {
                        left++;
                        while (left<right &&nums[left]==nums[left-1])
                        {
                            left++;
                        }
                    }
                    else
                    {
                        right--;
                        while (left<right &&nums[right]==nums[right+1])
                        {
                            right--;
                        }
                    }
                }
            }
            visitedAnchor.insert(anchor);
        }
        return res;
    }
};