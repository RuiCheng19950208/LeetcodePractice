// Definition for singly-linked list.
public class Solution1367 {
    private bool dfs(ListNode listNode, TreeNode treeNode)
    {
        if (listNode==null)
        {
            return true;
        }
        if (treeNode==null)
        {
            return false;
        }
        if (listNode.val!=treeNode.val)
        {
            return false;
            
        }
        return dfs(listNode.next,treeNode.right)||dfs(listNode.next,treeNode.left);
    }
    public bool IsSubPath(ListNode head, TreeNode root) 
    {
        LinkedList<TreeNode> theDeque = new LinkedList<TreeNode>();
        theDeque.AddLast(root);

        while (theDeque.Count>0)
        {
            TreeNode node = theDeque.First.Value;
            theDeque.RemoveFirst();
            if (dfs(head,node))
            {
                return true;
                
            }
            if (node.right!=null)
            {
                theDeque.AddLast(node.right);
            }
            if (node.left!=null)
            {
                theDeque.AddLast(node.left);
            }
        }

        return false;
    }
}