public class Solution108 {
    public TreeNode SortedArrayToBST(int[] nums) 
    {
        if(nums.Length==0){return null;}
        int mid = nums.Length/2;
        TreeNode root = new TreeNode(nums[mid]);
        int[] leftSubarray = nums.Take(mid).ToArray();
        int[] rightSubarray = nums.Skip(mid + 1).ToArray();
        root.left = SortedArrayToBST(leftSubarray);
        root.right = SortedArrayToBST(rightSubarray);
        return root;
        
    }
}