public class Solution45 {
    public int Jump(int[] nums) 
    {
        int step = 0;
        int curRight = 0;
        int maxRight = 0;
        for (int i = 0; i < nums.Length; i++)
        {
            if (i>curRight)
            {
                step++;
                curRight = maxRight;
            }
            if (maxRight<nums[i]+i)
            {
                maxRight = nums[i]+i;
                if (maxRight >= nums.Length-1 && i<nums.Length-1)
                {
                    return step;
                }
            }
        }
        return step+1;
        
    }
    
}