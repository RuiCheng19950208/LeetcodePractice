public class Solution26 {
    public int RemoveDuplicates(int[] nums) 
    {
        int slow = 0;
        for(int i=1; i< nums.Length;i++)
        {
            if (nums[i] != nums[slow])
            {
                slow++;
                nums[slow] = nums[i];
            }
        }
        return slow+1;
    }
}