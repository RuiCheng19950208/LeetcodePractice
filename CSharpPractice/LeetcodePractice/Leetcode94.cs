public class Solution94 {
    List<int> ans = new List<int>();  
    public void helper(TreeNode node)
    {
        if(node==null){return;}
        helper(node.left);
        ans.Add(node.val);
        helper(node.right);
        return;

    }
    public IList<int> InorderTraversal(TreeNode root) 
    {
        helper(root);
        return ans;
    }
}