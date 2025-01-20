let pnums;
let n;
let ans;
var helper = function(start,temp)
{
    ans.push([...temp]);
    for(let i=start;i<n;i++)
    {
        temp.push(pnums[i]);
        helper(i+1,temp);
        temp.pop();
    }

}
var subsets = function(nums) 
{
    ans=[];
    pnums=nums;
    n=nums.length;
    helper(0,[]);
    return ans;
};
