class Solution {
public:
    void rotate(vector<vector<int>>& matrix) {
        int topRight;
        int topLeft;
        int bottomRight;
        int bottomLeft;
        int n = matrix.size();
        for(int i=0; i<n/2;i++)
        {
            for(int j=i;j<n-i-1;j++)
            {
                topLeft = matrix[i][j];
                topRight = matrix[j][n-i-1];
                bottomRight = matrix[n-i-1][n-j-1];
                bottomLeft = matrix[n-j-1][i];

                matrix[i][j] = bottomLeft;
                matrix[j][n-i-1] =topLeft;
                matrix[n-i-1][n-j-1]= topRight;
                matrix[n-j-1][i]= bottomRight;
            }
        }
    }
};