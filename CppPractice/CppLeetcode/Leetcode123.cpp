class Solution {
public:
    int maxProfit(vector<int>& prices) 
    {
        vector<int> sells={0,0};
        vector<int> buys={-1000000,-1000000};
        int n = sells.size();
        for(int i=0;i<prices.size();i++)
        {
            for(int j=0;j<n;j++)
            {
                if(j==0){buys[j] = max(buys[j],-prices[i]);}
                else{buys[j] = max(buys[j],sells[j-1]-prices[i]);}
                sells[j] = max(buys[j]+prices[i],sells[j]);
            }
        }
        return sells[n-1];   
    }
};