public class Solution {
    public bool IsValidSudoku(char[][] board) {
        
        Dictionary<int,HashSet<int>> colSet  = new Dictionary<int,HashSet<int>>();
        Dictionary<int,HashSet<int>> rowSet  = new Dictionary<int,HashSet<int>>();
        Dictionary<int,HashSet<int>> boxIndexSet  = new Dictionary<int,HashSet<int>>();

        for (int i = 0; i < board.Length; i++)
        {
            for (int j = 0; j < board[0].Length; j++)
            {
                if (board[i][j]!='.')
                {
                    int theVal = board[i][j]-'0';
                    int boxIndex = 3*(i/3)+j/3;

                    if (!colSet.ContainsKey(j))
                    {
                        colSet[j] = new HashSet<int>();
                    }
                    if (!rowSet.ContainsKey(i))
                    {
                        rowSet[j] = new HashSet<int>();
                    }
                    if (!boxIndexSet.ContainsKey(boxIndex))
                    {
                        boxIndexSet[boxIndex] = new HashSet<int>();
                    }


                    bool isValid = !colSet[j].Contains(theVal)||!rowSet[i].Contains(theVal)||!boxIndexSet[boxIndex].Contains(theVal);
                    if (!isValid)
                    {
                        return false;
                    }
                    colSet[j].Add(theVal);
                    rowSet[i].Add(theVal);
                    boxIndexSet[boxIndex].Add(theVal);

                }
                
            }
            
        }

        return true;
        

    }
}