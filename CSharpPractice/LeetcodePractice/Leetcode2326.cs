using System.Xml.XPath;

public class Solution2326 {
    int[][] result;
    int directIndex = 0;
    Tuple<int,int>[] directions = new Tuple<int,int>[4] ; 

    int[] curPos  = new int[2];
    int publicm;
    int publicn;
    private void MoveToNext(int val)
    {
        result[curPos[0]][curPos[1]] = val;
        int nextRow = curPos[0]+ directions[directIndex].Item1;
        int nextCol = curPos[1]+ directions[directIndex].Item2;
        if (nextRow<0||nextRow>=publicm||nextCol<0||nextCol>=publicn||result[nextRow][nextCol]!=-1)
        {
            directIndex = (directIndex+1)%4;
            nextRow = curPos[0]+ directions[directIndex].Item1;
            nextCol = curPos[1]+ directions[directIndex].Item2;
        }
        curPos[0] = nextRow;
        curPos[1] = nextCol;

    }
    public int[][] SpiralMatrix(int m, int n, ListNode head) 
    {
        
        publicm=m;
        publicn=n;
        curPos[0]=0;
        curPos[1]=0;
        directions[0] = new Tuple<int, int>(0, 1);
        directions[1] = new Tuple<int, int>(1, 0);
        directions[2] = new Tuple<int, int>(0, -1);
        directions[3] = new Tuple<int, int>(-1, 0);

        result = new int[m][];
        for (int i = 0; i < m; i++)
        {
            int[] row = new int[n];
            Array.Fill(row,-1);
            result[i] = row;
        }
        while (head!=null)
        {
            MoveToNext(head.val);
            head = head.next;
        }
        return result;
    }
}