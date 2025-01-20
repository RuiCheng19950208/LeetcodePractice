public class Solution101_2 {
    bool helper(TreeNode node1,TreeNode node2)
    {
        if(node1==null && node2==null){return true;}
        if(node1==null || node2==null){return false;}
        return (helper(node1.right,node2.left) && helper(node1.left,node2.right) && node1.val==node2.val);
    }
    public bool IsSymmetric(TreeNode root) 
    {
        return helper(root.right,root.left);
    }
}