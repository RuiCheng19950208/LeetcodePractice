var twoSum = function(nums, target) 
{
    let map = {};
    for (let i = 0; i < nums.length; i++) {
       let complement = target  - nums[i];
       if (map[complement]!=undefined) 
       {
            return[i,map[complement]]
       }
       else
       {
            map[nums[i]] = i;
       }
    }
    return [];
    
};