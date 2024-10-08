public class Solution404 {
    public int helper(TreeNode node, bool flag)
    {
        if (node==null)
        {
            return 0;
        }
        if (node.right==null && node.left==null && flag)
        {
            return node.val;
        }
        else
        {
            return helper(node.left,true)+helper(node.right,false);
        }

    }
    public int SumOfLeftLeaves(TreeNode root) 
    {
        return helper(root.right,false)+helper(root.left,true);
        
    }
}