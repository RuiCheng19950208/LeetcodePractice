var findDisappearedNumbers = function(nums) 
{
    let ans=[]
    let n=nums.length;
    let s = new Set(nums);
    for(let i=1;i<=n;i++)
    {
        if(!s.has(i)){ans.push(i);}
    }
    return ans;
};