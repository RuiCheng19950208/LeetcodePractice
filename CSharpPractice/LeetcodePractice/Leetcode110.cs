public class Solution110 {
    int helper(TreeNode node)
    {
        if(node==null){return 0;}
        int rightH = helper(node.right);
        if(rightH==-1){return -1;}
        int leftH = helper(node.left);
        if(leftH==-1){return -1;}
        if(Math.Abs(rightH-leftH)>1){return -1;}
        return Math.Max(rightH,leftH)+1;
    }
    public bool IsBalanced(TreeNode root) 
    {
        if(root==null){return true;}
        return helper(root)!=-1;
    }
}