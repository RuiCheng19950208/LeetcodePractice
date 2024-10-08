class Solution {
public:
    bool canArrange(vector<int>& arr, int k) 
    {
        map<int,int> theMap;
        for(int i=0;i<k;i++){theMap[i]=0;}
        for(int a:arr)
        {
            if(a<0){while(a<0){a+=k;}}
            a=a%k;
            cout<<a<<endl;
            theMap[a]++;
        }
        for(auto pair:theMap)
        {
            if(pair.first==0 && pair.first%2!=0){return false;}
            if(pair.first!=0 && pair.first!=k-pair.first && theMap[pair.first]!=theMap[k-pair.first]){return false;}
            if(pair.first!=0 && pair.first==k-pair.first && theMap[pair.first]%2!=0){return false;}
        }
        return true;
        
    }
};