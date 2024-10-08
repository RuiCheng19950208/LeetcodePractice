public class Solution37 {
    Dictionary<int,HashSet<char>> colDic = new Dictionary<int, HashSet<char>>();
    Dictionary<int,HashSet<char>> rowDic = new Dictionary<int, HashSet<char>>();
    Dictionary<int,HashSet<char>> boxIndexDic = new Dictionary<int, HashSet<char>>();


    private bool isValid(int row,int col,char c)
    {
        int boxIndex = (row / 3) * 3 + col / 3;
        if (!rowDic[row].Contains(c)&&!colDic[col].Contains(c) && !boxIndexDic[boxIndex].Contains(c))
        {
            return true;
        }
        return false;
    }
    private bool dfs(int row,int col,ref char[][]board)
    {
        if (row==9)
        {
            return true;
        }
        else if (col==9)
        {
            return dfs(row+1,0,ref board);
        }
        else
        {
            if (board[row][col]!='.')
            {
                return dfs(row,col+1,ref board);
            }
            else
            {
                for (char c = '1'; c <= '9'; c++)
                {
                    if (isValid(row,col,c))
                    {
                        int boxIndex =3*(row/3)+col/3;
                        colDic[col].Add(c);
                        rowDic[row].Add(c);
                        boxIndexDic[boxIndex].Add(c);
                        board[row][col] = c;
                        if (dfs(row,col+1,ref board))
                        {
                            return true;
                        }
                        board[row][col] = '.';
                        colDic[col].Remove(c);
                        rowDic[row].Remove(c);
                        boxIndexDic[boxIndex].Remove(c);
                    }
                }
            }
        }
        return false;

    }
    public void SolveSudoku(char[][] board) {
        for (var i = 0; i < 9; i++)
        {
            colDic[i] = new HashSet<char>();
            rowDic[i] = new HashSet<char>();
            boxIndexDic[i] = new HashSet<char>();            
        }
        for (int i = 0; i < board.Length; i++)
            {
                for (int j = 0; j < board[0].Length; j++)
                {
                    if (board[i][j]!='.')
                    {
                        char c = board[i][j];
                        int boardIndex = 3*(i/3)+j/3;
                        rowDic[i].Add(c);
                        colDic[j].Add(c);
                        boxIndexDic[boardIndex].Add(c);            
                    }
                }
            }

        dfs(0,0,ref board);
        return;
        
    }
}