public class Solution530 {
    List<int> numList = new List<int>();
    public void helper(TreeNode node)
    {
        if(node==null){return;}
        numList.Add(node.val);
        helper(node.right);
        helper(node.left);
        return;
    }
    public int GetMinimumDifference(TreeNode root)
    {
        int ans=1000000;
        helper(root);
        numList.Sort();
        for(int i=1;i<numList.Count;i++)
        {
            int temp=numList[i]-numList[i-1];
            if(ans>temp){ans=temp;}

        }
        return ans;
    }
}
