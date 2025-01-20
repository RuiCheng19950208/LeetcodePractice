public class Solution27 {
    public int RemoveElement(int[] nums, int val) 
    {
        int slow =0;
        for(int i=0;i<nums.Length;i++)
        {
            if(nums[i]!=val)
            {
                int temp = nums[i];
                nums[i] = nums[slow];
                nums[slow] = temp;
                slow++;
            }
        }
        return slow;
        
    }
}