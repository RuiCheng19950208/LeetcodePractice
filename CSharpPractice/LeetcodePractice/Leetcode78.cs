public class Solution {
    public int[] pnums;
    public List<IList<int>> ans =  new List<IList<int>>();
    public int n=0;
    public void helper(int start,List<int> temp)
    {
        ans.Add(new List<int>(temp));
        for(int i=start;i<n;i++)
        {
            temp.Add(pnums[i]);
            helper(i+1,temp);
            temp.RemoveAt(temp.Count-1);
        }
    }

    public IList<IList<int>> Subsets(int[] nums) 
    {
        n = nums.Length;
        pnums = nums;
        List<int> temp=new List<int>();
        helper(0,temp);
        return ans;
    }
}