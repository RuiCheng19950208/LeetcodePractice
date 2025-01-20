public class Solution1829 {
    public int[] GetMaximumXor(int[] nums, int maximumBit) 
    {
        List<int> ans = new List<int>();
        int curXOR = 0;
        int theMax = (1<<maximumBit)-1;
        for(int i=0;i<nums.Length;i++)
        {
            if(i==0){curXOR = nums[0];}
            else{curXOR ^= nums[i];}
            ans.Add(theMax-curXOR);

        }
        ans.Reverse();
        return ans.ToArray();
        
    }
}