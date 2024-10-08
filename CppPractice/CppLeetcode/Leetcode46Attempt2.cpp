class Solution {
public:

    vector<vector<int>> ans;
    vector<int> numsPublic;
    void helper(vector<int> &temp)
    {
        if(temp.size()==numsPublic.size())
        {
            ans.push_back(temp);
        }
        for(int theNum:numsPublic)
        {
            if(find(temp.begin(),temp.end(),theNum)==temp.end())
            {
                temp.push_back(theNum);
                helper(temp);
                temp.pop_back();
            }
        }
    } 
    vector<vector<int>> permute(vector<int>& nums) 
    {
        vector<int> temp;
        numsPublic = nums;
        helper(temp);
        return ans;
        
    }
};