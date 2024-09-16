public class Solution52 {
    private int ans = 0;
    private int publicN;

    private HashSet<int> colSet = new HashSet<int>();
    private HashSet<int> PlusSet = new HashSet<int>();
    private HashSet<int> MinusSet = new HashSet<int>();

    private void dfs(int i)
    {
        if (i==publicN)
        {
            ans++;
            return;
        }
        else
        {
            for (int j = 0; j < publicN; j++)
            {
                if (isValid(i,j))
                {
                    colSet.Add(j);
                    PlusSet.Add(i+j);
                    MinusSet.Add(i-j);
                    dfs(i+1);
                    colSet.Remove(j);
                    PlusSet.Remove(i+j);
                    MinusSet.Remove(i-j);

                }
                    
            }
 
            
        }
        return;

    }
    private bool isValid(int i,int j)
    {
        if (colSet.Contains(j)|| PlusSet.Contains(i+j)||MinusSet.Contains(i-j))
        {
            return false;
        }
        else
        {
            return true;
        }
    } 
    public int TotalNQueens(int n) 
    {
        publicN = n;
        dfs(0);
        return ans;
        
    }
}