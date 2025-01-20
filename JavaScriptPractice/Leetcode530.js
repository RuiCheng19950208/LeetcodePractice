let nums;
var helper=function(node)
{
    if(node==null){return;}
    nums.push(node.val);
    helper(node.left);
    helper(node.right);
    return;

}
var getMinimumDifference = function(root) 
{
    nums=[];
    let ans=Infinity;
    let temp=0;
    helper(root);
    nums.sort((a,b)=>a-b);
    for(let i=1;i<nums.length;i++)
    {
        temp = nums[i]-nums[i-1];
        if(temp<ans){ans=temp;}
    }
    return ans;
};