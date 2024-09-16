var jump = function(nums) 
{
    let curRight = 0;
    let maxRight = 0;
    let step = 0;
    for (let i = 0; i < nums.length; i++) {
        if (i>curRight) 
        {
            curRight = maxRight;
            step++;
        }
        if (maxRight<nums[i]+i) 
        {
            maxRight=nums[i]+i;
            if (maxRight>=nums.length-1 && i!=nums.length-1) 
            {
                return step+1;
            }
        }
    }
    return step;
};