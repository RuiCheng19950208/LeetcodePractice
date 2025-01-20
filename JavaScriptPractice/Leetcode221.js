var maximalSquare = function(matrix) 
{
    let row = matrix.length;
    let col = matrix[0].length;
    let ans = 0;
    let dp = Array.from({length:row},()=>Array(col).fill(0));
    for(let i=0;i<row;i++)
    {
        for(let j=0;j<col;j++)
        {
            if(matrix[i][j]=='1')
            {
                if(i>0 & j>0)
                {
                    dp[i][j] = Math.min(dp[i-1][j-1],dp[i][j-1],dp[i-1][j])+1;
                }
                else{dp[i][j]=1;}
                ans=Math.max(ans,dp[i][j]);
            }
        }
    }
    return ans*ans;
};