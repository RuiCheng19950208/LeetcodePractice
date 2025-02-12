var uniquePathsWithObstacles = function(obstacleGrid) 
{
    let m = obstacleGrid.length;
    let n = obstacleGrid[0].length;
    let dp = Array.from({length:m},()=>Array(n).fill(0))
    if (obstacleGrid[0][0]==0) {
        dp[0][0]=1
    }
    for (let i = 1; i < m; i++) {
        if (obstacleGrid[i][0]==0) {
            dp[i][0] = dp[i-1][0];
            
        }
        
    }
    for (let j = 1; j < n; j++) {
        if (obstacleGrid[0][j]==0) {
            dp[0][j] = dp[0][j-1];
            
        }
        
    }
    for (let i = 0; i < m; i++) {
        for (let j = 0; j < n; j++) {
            if (obstacleGrid[i][j]==0) {
                dp[i][j] = dp[i][j-1]+dp[i-1][j];
                
            }
            
        }
        
    }
    return dp[m-1][n-1];

    
};