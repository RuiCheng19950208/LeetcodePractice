public class Solution2501 {
    public int LongestSquareStreak(int[] nums) 
    {
        Array.Sort(nums);
        HashSet<int> theSet = new HashSet<int>(nums);
        int ans=0;
        foreach(int num in nums)
        {
            long cur = num;
            int tempAns=1;
            while(true)
            {
                long next = cur*cur;
                if(next>int.MaxValue || !theSet.Contains((int)next)){break;}
                cur=next;
                tempAns++;

            }
            ans =Math.Max(ans,tempAns);
        }
        return ans>1?ans:-1;
    }
}