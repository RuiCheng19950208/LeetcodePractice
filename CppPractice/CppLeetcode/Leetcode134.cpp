class Solution {
public:
    int canCompleteCircuit(vector<int>& gas, vector<int>& cost) 
    {
        int ans=0;
        int curGas = 0;
        if(accumulate(gas.begin(),gas.end(),0)-accumulate(cost.begin(),cost.end(),0)<0){return -1;}
        for(int i=0;i<gas.size();i++)
        {
            curGas +=(gas[i]-cost[i]);
            if(curGas<0)
            {
                curGas=0;
                ans=i+1;
            }
        }
        return ans; 
    }
};