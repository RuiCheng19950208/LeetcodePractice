var rotate = function(matrix) {
    let n = matrix.length;
    let topLeft = 0;
    let topRight = 0;
    let bottomRight = 0;
    let bottomLeft = 0;
    for(let i=0;i<=n-2;i++)
    {
        for(let j =i;j<=n-2-i;j++)
        {
            topLeft = matrix[i][j];
            topRight = matrix[j][n-1-i];
            bottomRight = matrix[n-1-i][n-1-j];
            bottomLeft = matrix[n-1-j][i];

            matrix[i][j] = bottomLeft;
            matrix[j][n-1-i]= topLeft;
            matrix[n-1-i][n-1-j] = topRight;
            matrix[n-1-j][i] = bottomRight;
        }
    }
};