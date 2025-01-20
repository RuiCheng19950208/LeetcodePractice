class Solution {
public:
    int maximalSquare(vector<vector<char>>& matrix) 
    {
        int row = matrix.size();
        int col = matrix[0].size();
        int ans=0;
        vector<vector<int>> dp(row,vector<int>(col,0));
        for(int i=0;i<row;i++)
        {
            for(int j=0;j<col;j++)
            {
                if(matrix[i][j]=='1')
                {
                    if(i>0 && j>0)
                    {
                        dp[i][j]=min({dp[i-1][j-1],dp[i][j-1],dp[i-1][j]})+1;
                    }
                    else{dp[i][j]=1;}
                    ans = max(ans,dp[i][j]);
                }
            }
        }
        return ans*ans;
    }
};