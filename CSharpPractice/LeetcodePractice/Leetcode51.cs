using System.Runtime.Versioning;
using System.Security.Cryptography.X509Certificates;

public class Solution51
{
    HashSet<int> colSet = new HashSet<int>();
    HashSet<int> colPlusRowSet = new HashSet<int>();
    HashSet<int> colMinusRowSet = new HashSet<int>();
    List<IList<string>> ans  =new List<IList<string>>();

    char[,] board;

    int publicN ;
    public void dfs(int row)
    {
        if (row==publicN)
        {
            IList<string> curResult = new List<string>();
            for (int i = 0; i < publicN; i++)
            {
                string newLine = "";
                for (int j = 0; j < publicN; j++)
                {
                    newLine += board[i,j];
                }
                curResult.Add(newLine);
            }
            ans.Add(curResult);
            return;
        }
        else
        {
            for (int j = 0; j < publicN; j++)
            {
                if (isValid(row,j))
                {
                    colSet.Add(j);
                    colPlusRowSet.Add(row+j);
                    colMinusRowSet.Add(j-row);
                    board[row,j] = 'Q';

                    dfs(row+1);

                    colSet.Remove(j);
                    colPlusRowSet.Remove(row+j);
                    colMinusRowSet.Remove(j-row);
                    board[row,j] = '.';
                }
            }
        }
    }
    public bool isValid(int i, int j)
    {
        if (!colSet.Contains(j) && !colPlusRowSet.Contains(i+j) && !colMinusRowSet.Contains(j-i))
        {
            return true;
        }
        else
        {
            return false;
        }
    }
    public IList<IList<string>> SolveNQueens(int n) 
    {
        publicN =n;
        board = new char[n,n];
        
        for (int i = 0; i < n; i++)
        {
            for (int j =0;j <n;j++)
            {
                board[i,j] = '.'; 
            }
        }
        dfs(0);
        return ans;  
    }
}