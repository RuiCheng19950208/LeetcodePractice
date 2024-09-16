public class Solution54 {
    public IList<int> SpiralOrder(int[][] matrix) 
    {
        int m = matrix.Length;
        int n = matrix[0].Length;
        IList<int> res = new List<int>();
        List<Tuple<int,int>> directions = new List<Tuple<int, int>>();
        directions.Add(Tuple.Create(0,1));
        directions.Add(Tuple.Create(1,0));
        directions.Add(Tuple.Create(0,-1));
        directions.Add(Tuple.Create(-1,0));
        int directIndex =0;
        bool[,] visited = new bool[m,n];
        int step = m*n;
        int curRow = 0;
        int curCol = 0;
        while (step>0)
        {
            res.Add(matrix[curRow][curCol]);
            visited[curRow,curCol] = true;
            step--;
            int nextRow = curRow +directions[directIndex].Item1;
            int nextCol = curCol +directions[directIndex].Item2;
            if (nextRow<0||nextRow>m-1||nextCol<0||nextCol>n-1||visited[nextRow,nextCol] ==true)
            {
                directIndex = (directIndex+1)%4;
            }
            curRow = curRow +directions[directIndex].Item1;
            curCol = curCol +directions[directIndex].Item2;
        }
        return res;
    }
}