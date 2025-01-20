var canCompleteCircuit = function(gas, cost) 
{
    if(gas.reduce((a,b)=>a+b,0)-cost.reduce((a,b)=>a+b,0)<0){return -1;}
    let ans = 0;
    let curGas = 0;
    for(let i=0;i<cost.length;i++)
    {
        curGas +=(gas[i]-cost[i]);
        if(curGas<0)
        {
            curGas=0;
            ans=i+1;
        }

    }
    return ans;
};