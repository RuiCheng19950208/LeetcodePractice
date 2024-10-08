class Solution {
public:
    vector<int> arrayRankTransform(vector<int>& arr) 
    {
        vector<int> ans;
        
        vector<int> sortArr=arr;
        sort(sortArr.begin(),sortArr.end());
        unordered_map<int,int> theMap;
        int rank=1;
        for(int i=0;i<sortArr.size();i++)
        {
            if(theMap.find(sortArr[i])==theMap.end())
            {
                theMap[sortArr[i]] = rank;
                rank++;
            }
        }
        for(int num:arr)
        {
            ans.push_back(theMap[num]);
        }
        return ans;
        
    }
};