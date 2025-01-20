class Solution {
public:
    vector<vector<int>> dfs;
    vector<vector<int>> grid;
    int row;
    int col;
    vector<pair<int,int>> directs = {{-1,1},{0,1},{1,1}};

    int helper(int row,int col)
    {
        if (col==this->col-1){return 0;}
        if (this->dfs[row][col]!=-1){return this->dfs[row][col];}
        int temp=0;
        for(auto dire:directs)
        {
            int newRow = row+dire.first;
            int newCol = col+dire.second;
            if(newRow>=0 && newRow<this->row && newCol>=0 && newCol<this->col && this->grid[newRow][newCol]>this->grid[row][col])
            {
                temp = max(temp,1+helper(newRow,newCol));
            }
        }
        this->dfs[row][col]=temp;
        return temp;
    }
    int maxMoves(vector<vector<int>>& grid) 
    {
        this->grid = grid;
        this->row = grid.size();
        this->col = grid[0].size();
        this->dfs = vector<vector<int>>(row,vector<int>(col,-1));
        int ans=0;
        for(int i=0;i<this->row;i++)
        {
            ans=max(ans,helper(i,0));
        }
        return ans;
    }
};