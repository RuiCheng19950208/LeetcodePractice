let ans=0;
var helper = function(node)
{
    if(node==null){return 0 ;}
    let leftSum = Math.max(0,helper(node.left));
    let rightSum = Math.max(0,helper(node.right));
    let tempAns = node.val + leftSum + rightSum;
    ans =Math.max(ans,tempAns);
    return node.val + Math.max(leftSum,rightSum);
};
var maxPathSum = function(root) 
{
    ans=-10000;
    helper(root);
    return ans;
};