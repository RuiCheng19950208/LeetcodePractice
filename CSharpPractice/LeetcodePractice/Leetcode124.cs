public class Solution124 {
    int ans=-10000;
    public int helper(TreeNode node)
    {
        if(node==null){return 0;}
        int leftSum = Math.Max(0,helper(node.left));
        int rightSum = Math.Max(0,helper(node.right));
        int tempAns = node.val + leftSum + rightSum;
        ans=Math.Max(ans,tempAns);
        return node.val + Math.Max(leftSum,rightSum);
    }
    public int MaxPathSum(TreeNode root) 
    {
        helper(root);
        return ans;
    }
}