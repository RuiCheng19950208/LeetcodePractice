using System.Runtime.InteropServices.Marshalling;

public class Solution463
{
    public int ans = 0;
    public int IslandPerimeter(int[][] grid) {
        for (int i = 0; i < grid.Length; i++)
        {
            for (int j = 0; j < grid[0].Length; j++)
            {
                if (grid[i][j]==1)
                {
                    if (i==0 || grid[i-1][j]==0)
                    {
                        ans++;
                    }
                    if (i==grid.Length-1 || grid[i+1][j]==0)
                    {
                        ans++;
                    }
                    if (j==0 || grid[i][j-1]==0)
                    {
                        ans++;
                    }
                    if (j==grid[0].Length-1 || grid[i][j+1]==0)
                    {
                        ans++;
                    }
                    
                }
                
            }
            
        }


        return ans;
        
    }
}