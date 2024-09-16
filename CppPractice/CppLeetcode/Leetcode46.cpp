#include<vector>
using namespace std;

class Solution {
private:
    void helper(vector<int> &nums,vector<int> &temp,vector<vector<int>> &result)
    {
        if (temp.size() == nums.size())
        {
            result.push_back(temp);
        }
        for (int i = 0; i < nums.size(); i++)
        {
            if (find(temp.begin(),temp.end(),nums[i])==temp.end())
            {
                temp.push_back(nums[i]);
                helper(nums,temp,result);
                temp.pop_back();
            }
        }
    }
public:
    vector<vector<int>> permute(vector<int>& nums) 
    {
        vector<vector<int>> result;
        vector<int> temp;
        
        helper(nums,temp,result);

        return result;
    }
};