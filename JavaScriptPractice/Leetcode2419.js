var longestSubarray = function(nums) 
{
    let maxVal = Math.max(...nums)
    let ans=0;
    let temp=0
    for(let num of nums)
    {
        if (num==maxVal) {
            temp++
            ans=Math.max(ans,temp)
        }
        else 
        {
            temp=0
        }
    }
    return ans
};