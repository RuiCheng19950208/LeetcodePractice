public class Solution2684 {
    private int[,] grid;
    private int[,] dfs;
    private int row,col;
    private int[,] directions = {{-1,1},{0,1},{1,1}};
    public int helper(int row,int col)
    {
        if(col==this.col-1){return 0;}
        if(this.dfs[row,col]!=-1){return this.dfs[row,col];}
        int temp=0;
        for(int i=0; i< this.directions.GetLength(0);i++)
        {
            int newRow = row + directions[i,0];
            int newCol = col + directions[i,1];
            if(newRow>=0 && newRow<this.row && newCol >=0 && newCol <this.col && this.grid[newRow,newCol]>this.grid[row,col])
            {temp = Math.Max(temp,1+helper(newRow,newCol));}
        }
        this.dfs[row,col] = temp;
        return temp;
    }
    public int MaxMoves(int[][] grid) 
    {
        this.row = grid.Length;
        this.col = grid[0].Length;
        this.grid = new int[this.row, this.col];
        this.dfs = new int[this.row, this.col];
        for(int i=0;i<this.row;i++)
        {
            for(int j=0;j<this.col;j++){this.grid[i,j]=grid[i][j];}
        } 

        for(int i=0;i<this.row;i++)
        {
            for(int j=0;j<this.col;j++){this.dfs[i,j]=-1;}
        } 
        int ans=0;
        for(int i=0;i<this.row;i++){ans= Math.Max(ans,helper(i,0));}
        return ans;
    }
}