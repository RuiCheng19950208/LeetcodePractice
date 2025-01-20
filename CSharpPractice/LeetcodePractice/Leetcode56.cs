public class Solution56 {
    public int[][] Merge(int[][] intervals) 
    {
        List<int[]> ans =new List<int[]>();
        Array.Sort(intervals,(a,b)=>a[0].CompareTo(b[0]));
        int[] temp = intervals[0];
        for(int i=1;i<intervals.Length;i++)
        {
            if(intervals[i][0]<=temp[1])
            {
                temp[0] = Math.Min(temp[0],intervals[i][0]);
                temp[1] = Math.Max(temp[1],intervals[i][1]);

            }
            else
            {
                ans.Add(temp);
                temp=intervals[i];
            }
        }
        ans.Add(temp);
        return ans.ToArray();
    }
}