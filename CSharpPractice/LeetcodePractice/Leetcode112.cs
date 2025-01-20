public class Solution112 {
    public bool HasPathSum(TreeNode root, int targetSum) 
    {
        if(root==null){return false;}
        LinkedList<Tuple<TreeNode,int>> q = new LinkedList<Tuple<TreeNode,int>>();
        q.AddLast(new Tuple<TreeNode,int>(root,root.val));
        
        while(q.Count >0)
        {
            TreeNode curNode = q.First.Value.Item1;
            int curSum = q.First.Value.Item2;
            q.RemoveFirst();
            if(curNode.right==null && curNode.left==null&&curSum==targetSum)
            {
                return true;
            }
            if(curNode.left!=null)
            {
                q.AddLast(new Tuple<TreeNode,int>(curNode.left,curSum + curNode.left.val));
            }
            if(curNode.right!=null)
            {
                q.AddLast(new Tuple<TreeNode,int>(curNode.right,curSum + curNode.right.val));
            }
        }
        return false;
    }
}