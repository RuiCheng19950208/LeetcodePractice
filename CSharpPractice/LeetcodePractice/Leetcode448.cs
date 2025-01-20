public class Solution448 {
    public IList<int> FindDisappearedNumbers(int[] nums) 
    {
        List<int> ans = new List<int>();
        int n = nums.Length;
        HashSet<int> s = new HashSet<int>(nums);
        for(int i=1;i<=n;i++)
        {
            if(!s.Contains(i)){ans.Add(i);}
        }
        return ans;
    }
}