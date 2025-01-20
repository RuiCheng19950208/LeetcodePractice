public class Solution2425 {
    public int XorAllNums(int[] nums1, int[] nums2) 
    {
        int xor1=0;
        int xor2=0;

        foreach(int num in nums1)
        {
            xor1 ^= num;

        }
        foreach(int num in nums2)
        {
            xor2 ^= num;

        }


        if(nums1.Length%2 ==0 && nums2.Length%2 ==0 )
        {
            return 0;
        }
        else if(nums1.Length%2 ==0)
        {
            return xor1;
        }
        else if(nums2.Length%2 ==0)
        {
            return xor2;
        }
        else
        {
            return xor1 ^ xor2;

        }
        
    }
}