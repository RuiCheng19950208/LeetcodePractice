class Solution {
public:
    int n;
    vector<int> pnums;
    vector<vector<int>> ans;
    set<vector<int>> checkSet;
    void helper(int start, vector<int>temp)
    {
        if(checkSet.find(temp)==checkSet.end()){checkSet.insert(temp);ans.push_back(temp);}
        for(int i=start;i<n;i++)
        {
            temp.push_back(pnums[i]);
            helper(i+1,temp);
            temp.pop_back();
        }
    }
    vector<vector<int>> subsets(vector<int>& nums) 
    {
        pnums = nums;
        n= nums.size();
        vector<int> temp;
        helper(0,temp);
        return ans;
    }
};