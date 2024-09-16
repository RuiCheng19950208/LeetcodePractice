public class Solution200 {

    public void bfs(int i, int j, char[][]grid)
    {
        if(i<0 || j<0 || i >= grid.Length || j>=grid[0].Length)
        {
            return;
        }
        else
        {
            if(grid[i][j]=='1')
            {
                grid[i][j] = '0';
                bfs(i+1,j,grid);
                bfs(i-1,j,grid);
                bfs(i,j+1,grid);
                bfs(i,j-1,grid);
            }

        }

    }
    public int NumIslands(char[][] grid) 
    {
        int ans=0;
        for(int i=0;i<grid.Length;i++)
        {
            for(int j=0;j<grid[0].Length;j++)
            {
                if(grid[i][j]=='1')
                {
                    ans+=1;
                    bfs(i,j,grid);
                }
            }
        }
        return ans;
        
    }


    
}