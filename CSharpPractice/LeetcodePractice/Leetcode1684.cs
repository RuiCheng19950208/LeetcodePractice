public class Solution1684 {
    public int CountConsistentStrings(string allowed, string[] words) 
    {
        int ans=0;
        HashSet<char> goalSet  =new HashSet<char>(allowed);
        foreach (string word in words)
        {
            HashSet<char> tempSet = new HashSet<char>(word);

                if (tempSet.IsSubsetOf(goalSet))
                {
                    ans++;
                }
        }
        return ans;
    }
}