var helper=function(node,flag)
{
    if (node==null)
    {
        return 0;
    }
    if (node.right==null && node.left ==null && flag) {
        return node.val;
    }
    else 
    {
        return helper(ndoe.right,false)+helper(node.left,true)
    }
}
var sumOfLeftLeaves = function(root) {
    return helper(toot,false);
};