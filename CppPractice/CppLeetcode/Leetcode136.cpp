class Solution {
public:
    int singleNumber(vector<int>& nums) 
    {
        unordered_map<int,int> theMap;
        for(int num:nums)
        {
            if(theMap.find(num)==theMap.end()){theMap[num]=1;}
            else{theMap[num]+=1;}
        }
        for(auto pair:theMap)
        {if(pair.second==1){return pair.first;}}
        return -1;
    }
};