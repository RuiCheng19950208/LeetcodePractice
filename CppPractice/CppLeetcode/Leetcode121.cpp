class Solution {
public:
    int maxProfit(vector<int>& prices) {
        int ans=0;
        int curLow = prices[0];
        for(int i=1;i<prices.size();i++)
        {
            if(prices[i]<curLow){curLow=prices[i];}
            ans=max(ans,prices[i]-curLow);

            
        }
        return ans;
        
    }
};