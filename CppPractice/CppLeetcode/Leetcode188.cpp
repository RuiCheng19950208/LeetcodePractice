class Solution {
public:
    int maxProfit(int k, vector<int>& prices) 
    {
        vector<int> sells;
        vector<int> buys;
        for(int i=0;i<k;i++)
        {
            sells.push_back(0);
            buys.push_back(-1000000);
        }
        for(int i=0;i<prices.size();i++)
        {
            for(int j=0;j<k;j++)
            {
                if(j==0){buys[j]=max(buys[j], - prices[i]);}
                else{buys[j]=max(buys[j],sells[j-1] - prices[i]);}
                sells[j]=max(sells[j],buys[j]+prices[i]);
            }
        }
        return sells[k-1];
    }
};