public class Solution452 {
    public int FindMinArrowShots(int[][] points) 
    {
        Array.Sort(points,(a,b)=>a[1].CompareTo(b[1]));
        int ans=1;
        int end= points[0][1];
        if(points.Length<1){return 0;}
        for(int i=1;i<points.Length;i++)
        {
            if(points[i][0]>end)
            {
                end=points[i][1];
                ans++;
            }
        }
        return ans;
    }
}