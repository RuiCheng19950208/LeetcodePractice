#include<vector>
using namespace std;

class Solution {
private:
    void helper(vector<int> &valTemp,vector<int> &indexTemp, vector<vector<int>> &result, const vector<int> nums)
    {
        if (valTemp.size() == nums.size() && find(result.begin(),result.end(),valTemp)==result.end())
        {
            result.push_back(valTemp);
            return;
        }
        for (int i = 0; i < nums.size(); i++)
        {
            if (find(indexTemp.begin(),indexTemp.end(),i)==indexTemp.end())
            {
                indexTemp.push_back(i);
                valTemp.push_back(nums[i]);
                helper(valTemp,indexTemp,result,nums);
                valTemp.pop_back();
                indexTemp.pop_back();
            }
        }
        return;
        
    }
public:
    vector<vector<int>> permuteUnique(vector<int>& nums) 
    {
        vector<vector<int>> result;
        vector<int> valTemp;
        vector<int> indexTemp;
        helper(valTemp,indexTemp,result,nums);
        return result;
    }
};