public class Solution135 {
    public int Candy(int[] ratings) 
    {
        if(ratings.Length<2){return 1;}
        int[] ans = Enumerable.Repeat(1,ratings.Length).ToArray();
        for(int i=1;i<ratings.Length;i++)
        {
            if(ratings[i]>ratings[i-1]){ans[i] = ans[i-1]+1;}
        }
        for(int i=ratings.Length-2;i>=0;i--)
        {
            if(ratings[i]>ratings[i+1]){ans[i] = Math.Max(ans[i],ans[i+1]+1);}
        }
        return ans.Sum();
    }
}