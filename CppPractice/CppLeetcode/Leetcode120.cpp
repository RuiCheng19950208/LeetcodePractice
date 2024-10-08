class Solution {
public:
    int minimumTotal(vector<vector<int>>& triangle) 
    {
        vector<vector<int>> dp = triangle;
        for(int i=1;i<triangle.size();i++)
        {
            for(int j=0;j<triangle[i].size();j++)
            {
                if(j==0){dp[i][j]=dp[i-1][0]+triangle[i][j];}
                else if(j==i){dp[i][j]=dp[i-1][j-1]+triangle[i][j];}
                else{dp[i][j] = triangle[i][j ] +min(dp[i-1][j-1],dp[i-1][j]);}

            }

        }
        return *min_element(dp[dp.size()-1].begin(),dp[dp.size()-1].end());
        
    }
};