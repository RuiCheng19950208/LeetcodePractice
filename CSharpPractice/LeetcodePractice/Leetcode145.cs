public class Solution145 {
    List<int> ans = new List<int>();
    public void helper(TreeNode node)
    {
        if(node ==null){return;}
        helper(node.left);
        helper(node.right);
        ans.Add(node.val);

    }
    public IList<int> PostorderTraversal(TreeNode root) 
    {
        helper(root);
        return ans;
        
    }
}