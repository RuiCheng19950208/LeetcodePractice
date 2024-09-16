public class Solution2022 {
    public int[][] Construct2DArray(int[] original, int m, int n) 
    {
        int index = 0;
        int[][] ans =new int[m][];
        for (var i = 0; i < m; i++)
        {
            int[] tempList = new int[n];
            for (int j = 0; j < n; j++)
            {
                tempList[j] = original[index];
                index ++;
            }
            ans[i] = tempList;
        }

        return ans;
        
    }
}