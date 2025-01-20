var rob = function(nums) 
{
    let dp= new Array(nums.length+2).fill(0);
    for(let i=2;i<dp.length;i++)
    {
        dp[i]=Math.max(dp[i-1],dp[i-2]+nums[i-2]);
    }
    return dp[dp.length-1];
};