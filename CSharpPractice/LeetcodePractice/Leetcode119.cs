public class Solution119 {
    public IList<int> GetRow(int rowIndex) 
    {
        List<int> temp = new List<int>{1};
        List<int> ans = new List<int>{1,1};
        if(rowIndex==0){return temp;}
        if(rowIndex==1){return ans;}
        
        for(int i=0;i<rowIndex-1;i++)
        {
            temp = new List<int>{1};
            for(int j =1;j<i+2;j++)
            {
                temp.Add(ans[j-1]+ans[j]);
            }
            temp.Add(1);
            ans=temp;
        }
        return ans;        
    }
}