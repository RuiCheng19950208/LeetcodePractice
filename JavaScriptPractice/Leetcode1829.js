var getMaximumXor = function(nums, maximumBit) 
{
    let curXOR=0;
    let theMax = (1<<maximumBit)-1;
    let ans=[];
    for(let i=0;i<nums.length;i++)
    {
        if(i==0){curXOR=nums[0];}
        else{curXOR ^= nums[i];}
        ans.push(theMax-curXOR);

    }
    ans.reverse();
    return ans;
    
};