var maxSubArray = function(nums) 
{
    let curMax = nums[0]
    let res= curMax
    if (nums.length==1) {
        return res;
    }
    for (let i = 1; i < nums.length; i++) {
        curMax = Math.max(curMax+nums[i],nums[i]);
        res=Math.max(res,curMax)
    }
    return res;
};