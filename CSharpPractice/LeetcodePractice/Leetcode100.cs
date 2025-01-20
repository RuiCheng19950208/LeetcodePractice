public class Solution100 {
    public bool IsSameTree(TreeNode p, TreeNode q) 
    {
        if(p==null && q==null){return true;}
        else if(p==null || q==null){return false;}
        else{return p.val==q.val && IsSameTree(p.right,q.right) && IsSameTree(p.left,q.left); }
        
    }
}