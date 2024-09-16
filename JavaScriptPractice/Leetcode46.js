let result;
let temp;
let numsLen;

function helper(nums)
{
    if (temp.length==numsLen) 
    {
        result.push([...temp]);
    }
    for (let i = 0; i < nums.length; i++) 
    {
        if (!temp.includes(nums[i])) 
        {
            temp.push(nums[i]);
            helper(nums);
            temp.pop();
        }
    }
}
var permute = function(nums) 
{
    result=[];
    temp = [];
    numsLen = nums.length;
    helper(nums)

    return result;
    
};