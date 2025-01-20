public class Solution48 {
    public void Rotate(int[][] matrix) 
    {
        int n = matrix.Length;
        int topLeft = 0;
        int topRight = 0;
        int bottomRight = 0;
        int bottomLeft = 0;
        for(int i=0;i<=n-2;i++)
        {
            for(int j=i;j<=n-2-i;j++)
            {
                topLeft = matrix[i][j];
                topRight = matrix[j][n-1-i];
                bottomRight  = matrix[n-1-i][n-1-j];
                bottomLeft = matrix[n-1-j][i];

                matrix[i][j] = bottomLeft ;
                matrix[j][n-1-i] = topLeft;
                matrix[n-1-i][n-1-j] = topRight;
                matrix[n-1-j][i]=bottomRight;
            }
        }
    }
}