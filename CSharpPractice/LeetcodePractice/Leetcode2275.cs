public class Solution2275 {
    public int LargestCombination(int[] candidates) 
    {
        int ans=0;
        int temp=0;
        for(int i=0;i<32;i++)
        {
            temp=0;
            foreach(int num in candidates)
            {
                if((num&(1<<i))!=0){temp++;}
            }
            ans=Math.Max(temp,ans);
        }
        return ans;
    }
}