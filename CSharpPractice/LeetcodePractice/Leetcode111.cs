public class Solution111 {
    public int MinDepth(TreeNode root) 
    {
        if(root==null){return 0;}
        LinkedList<Tuple<TreeNode,int>> q = new LinkedList<Tuple<TreeNode,int>>();
        q.AddFirst(new Tuple<TreeNode,int>(root,1));
        while(q.Count>0)
        {
            TreeNode curNode = q.First.Value.Item1;
            int curDepth = q.First.Value.Item2;
            q.RemoveFirst();
            if(curNode.right==null && curNode.left==null){return curDepth;}
            if(curNode.right!=null){q.AddLast(new Tuple<TreeNode,int>(curNode.right,curDepth+1));}
            if(curNode.left!=null){q.AddLast(new Tuple<TreeNode,int>(curNode.left,curDepth+1));}
        }
        return -1;
    }
}