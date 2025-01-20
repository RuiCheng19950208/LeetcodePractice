public class Solution144 {
    List<int> ans = new List<int>();
    private void helper(TreeNode node)
    {
        if(node==null){return;}
        ans.Add(node.val);
        helper(node.left);
        helper(node.right);
        return;

    }
    public IList<int> PreorderTraversal(TreeNode root) 
    {
        helper(root);
        return ans;
        
    }
}