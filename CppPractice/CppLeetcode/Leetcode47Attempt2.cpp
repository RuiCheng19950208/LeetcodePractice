// It should work with swap();
#include<vector>
using namespace std;
class Solution {
public:
    vector<vector<int>> ans;
    vector<vector<int>> visited;
    vector<int> numsPublic;
    int n;
    void helper(vector<int> &temp,vector<int> &indexTemp)
    {
        if(temp.size()==n)
        {
            if(find(ans.begin(),ans.end(),temp)==ans.end())
            {   
                visited.push_back(indexTemp);
                ans.push_back(temp);
                return;
            }
            return;
        }
        for(int i=0;i<n;i++)
        {
            if(find(indexTemp.begin(),indexTemp.end(),i)==indexTemp.end())
            {
                temp.push_back(numsPublic[i]);
                indexTemp.push_back(i);
                helper(temp,indexTemp);
                indexTemp.pop_back();
                temp.pop_back();
            }
        }
        return;
    }
    vector<vector<int>> permuteUnique(vector<int>& nums) 
    {
        numsPublic = nums;
        n=nums.size();
        vector<int> temp;
        vector<int> indexTemp;
        helper(temp,indexTemp);
        return ans;
    }
};