class Solution {
public:
    vector<vector<int>> ans;
    vector<bool> visited;
    vector<int> numsPublic;
    int n;
    void helper(vector<int> &temp)
    {
        if(temp.size()==n)
        {
            ans.push_back(temp);
            return;
        }
        for(int i=0;i<n;i++)
        {
            if(i>0 && numsPublic[i]==numsPublic[i-1] && visited[i-1]==true ){continue;}
            if(!visited[i])
            {
                temp.push_back(numsPublic[i]);
                visited[i]=true;
                helper(temp);
                visited[i]=false;
                temp.pop_back();
            }
        }
        return;
    }
    vector<vector<int>> permuteUnique(vector<int>& nums) 
    {
        sort(nums.begin(),nums.end());
        numsPublic = nums;
        n=nums.size();
        vector<int> temp;
        visited  =vector<bool>(n,false);
        helper(temp);
        return ans;
    }
};