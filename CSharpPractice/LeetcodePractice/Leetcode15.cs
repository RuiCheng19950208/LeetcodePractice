public class Solution15 {
    public IList<IList<int>> ThreeSum(int[] nums) 
    {
        IList<IList<int>> res= new List<IList<int>>();
        int left = 0;
        int right = 0;
        int lenN = nums.Length;
        int theSum = 0;
        Array.Sort(nums);

        
        for (int i = 0; i < lenN; i++)
        {
            if (i>0 && nums[i-1]==nums[i])
            {
                continue;
            }
            left = i+1;
            right=lenN-1;
            while (left<right)
            {
                theSum = nums[i]+nums[left]+nums[right];
                if (theSum == 0)
                {
                    List<int> temp = new List<int>{nums[i],nums[left],nums[right]};
                    res.Add(temp);
                    left++;
                    while (left<right && nums[left]==nums[left-1])
                    {
                        left++;
                    }
                    right--;
                    while (left<right && nums[right]==nums[right+1])
                    {
                        right--;
                    }
                }
                else if (theSum<0)
                {
                    left++;
                    while (left<right && nums[left]==nums[left-1])
                    {
                        left++;
                    }
                    
                }
                else
                {
                    right--;
                    while (left<right && nums[right]==nums[right+1])
                    {
                        right--;
                    }
                }
            }
        }
        
        return res;

    }
}