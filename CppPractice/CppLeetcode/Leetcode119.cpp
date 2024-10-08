class Solution {
public:
    vector<int> getRow(int rowIndex) {
        if(rowIndex==0){return {1};}
        if(rowIndex==1){return {1,1};}
        vector<int> temp={1,1};
        for(int i=2;i<rowIndex+1;i++)
        {
            vector<int> newTemp = temp;
            newTemp.push_back(1);
            for(int j=1;j<newTemp.size()-1;j++){newTemp[j]=temp[j]+temp[j-1];}
            temp= newTemp;

        }
        return temp;

        
    }
};