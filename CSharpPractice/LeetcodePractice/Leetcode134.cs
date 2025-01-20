public class Solution134 {
    public int CanCompleteCircuit(int[] gas, int[] cost) 
    {

        if(gas.Sum()-cost.Sum()<0){return -1;}
        int ans=0;
        int curGas=0;
        for(int i=0;i<gas.Length;i++)
        {
            curGas +=(gas[i]-cost[i]);
            if(curGas<0)
            {
                ans=i+1;
                curGas=0;
            }

        }
        return ans;
        
    }
}