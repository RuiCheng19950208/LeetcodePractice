public class Solution386 {
    public IList<int> LexicalOrder(int n) {
        List<int> ans = new List<int>();
        for (var i = 1; i < n+1; i++)
        {
            ans.Add(i);
        }
        ans = ans.OrderBy(x=>x.ToString()).ToList();

        // ans.Sort((a,b)=>a.ToString().CompareTo(b.ToString())); It also works

        return ans;
    }
}