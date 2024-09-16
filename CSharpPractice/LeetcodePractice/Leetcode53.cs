public class Solution53 {
    public int MaxSubArray(int[] nums) 
    {
        int curMax =nums[0];
        int res = curMax;
        if (nums.Length==1)
        {
            return res;
        }
        for (int i = 1; i < nums.Length; i++)
        {
            curMax = Math.Max(curMax+nums[i],nums[i]);
            res =Math.Max(curMax,res);
        }
        return res;
    }
}