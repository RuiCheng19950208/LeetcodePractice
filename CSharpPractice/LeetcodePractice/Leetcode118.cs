public class Solution118 {
    public IList<IList<int>> Generate(int numRows) 
    {
        List<IList<int>> ans = new List<IList<int>>();
        List<int> temp = new List<int>{1};
        ans.Add(new List<int>(temp));
        if(numRows==1){return ans;}
        temp.Add(1);
        ans.Add(new List<int>(temp));
        if(numRows==2){return ans;}
        for(int i=0;i<numRows-2;i++)
        {
            List<int> newLine = new List<int>{1};
            for(int j=1;j<i+2;j++)
            {
                newLine.Add(temp[j-1]+temp[j]);

            }
            newLine.Add(1);
            temp = newLine;
            ans.Add(temp);
        }
        return ans;        
    }
}