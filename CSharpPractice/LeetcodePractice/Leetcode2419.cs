public class Solution2419{
    public int LongestSubarray(int[] nums) {
        int maxVal = nums.Max();
        int ans=0;
        int temp = 0;
        foreach (var num in nums)
        {
            if (num==maxVal)
            {
                temp++;
                ans= Math.Max(ans,temp);
            }
            else
            {
                temp=0;
            }
        }
        return ans;
    }
}