


public class Solution101 {
    public bool Solution101Helper(TreeNode p1,TreeNode p2)
    {
        if(p1==null && p2==null)
        {
            return true;
        }
        else if (p1==null || p2==null)
        {
            return false;
        }
        else
        {
            return (p1.val==p2.val && Solution101Helper(p1.right,p2.left) && Solution101Helper(p1.left,p2.right));
        }
    }
    public bool IsSymmetric(TreeNode root) 
    {
        if (root==null )
        {
            return true;   
        }
        else
        {
            return Solution101Helper(root.right,root.left);
        }
        
    }
}