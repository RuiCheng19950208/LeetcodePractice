class Solution {
public:
    vector<vector<int>> generate(int numRows) {
        vector<vector<int>> ans={{1},{1,1}};
        vector<int> temp={1,1};
        if(numRows==1){return {{1}};}
        if(numRows==2){return {{1},{1,1}};}
        for(int i=2;i<numRows;i++)
        {
            vector<int> newTemp = temp;
            newTemp.push_back(1);
            for(int j=1;j<newTemp.size()-1;j++){newTemp[j]=temp[j]+temp[j-1];}
            ans.push_back(newTemp);
            temp = newTemp;
            // cout<<temp<<endl;
        }
        return ans;
        
    }
};