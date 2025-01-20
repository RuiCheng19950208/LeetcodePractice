let publicRow;
let publicCol;
let publicGrid;
let directions;
let dfs;

var helper = function(row,col)
{
    if(col==publicCol-1){return 0;}
    if(dfs[row][col]!=-1){return dfs[row][col];}
    let temp=0;
    for(let i=0;i<directions.length;i++)
    {
        let newRow = row+directions[i][0];
        let newCol = col+directions[i][1];
        if(newRow>=0 && newRow<publicRow && newCol>=0 && newCol<publicCol && publicGrid[newRow][newCol]>publicGrid[row][col])
        {
            temp=Math.max(temp,1+helper(newRow,newCol));
        }
    }
    dfs[row][col] = temp;
    return temp;

}
var maxMoves = function(grid) 
{
    publicGrid = grid;
    publicRow = grid.length;
    publicCol = grid[0].length;
    directions = [[-1,1],[0,1],[1,1]];
    dfs = Array.from({length:publicRow},()=>Array(publicCol).fill(-1));
    let ans=0;
    for(let i=0;i<publicRow;i++){ans = Math.max(ans,helper(i,0));}
    return ans;
};