public class Solution35 {
    public int SearchInsert(int[] nums, int target) 
    {
        int left = 0;
        int right = nums.Length-1;
        int mid=0;
        int prevmid =0;
        while(left<=right)
        {
            mid = (left+right)/2;
            if(nums[mid]<target)
            {
                left =mid;
            }
            else
            {
                right = mid;
            }
            if(mid==prevmid)
            {
                if(nums[right]<target)
                {
                    return right +1;
                }
                else if(nums[left]>=target)
                {
                    return 0;
                }
                else
                {
                    return right;
                }

            }
            else
            {
                prevmid = mid;
            }

        }
        return 0;
    }
}