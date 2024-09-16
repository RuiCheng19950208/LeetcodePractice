#include <map>
#include <vector>

using namespace std;

class Solution {
public:
    vector<int> twoSum(vector<int>& nums, int target) 
    {
        vector<int> ans;
        map<int,int> theMap;
        for (int i = 0; i < nums.size(); i++)
        {
            int complement = target - nums[i];
            if (theMap.find(complement)!=theMap.end())
            {
                return {i,theMap[complement]};
            }
            else
            {

                theMap[nums[i]] = i ;

            }
            
            
        }

        vector<int> empty;
        return empty;
        
        
    }
};