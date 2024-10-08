public class TrieNode
{
    public int value = 0;
    public  Dictionary<char,TrieNode> nextChar = new Dictionary<char, TrieNode>();

}
public class Solution2416 {
    public int[] SumPrefixScores(string[] words) 
    {
        TrieNode root = new TrieNode();
        TrieNode curNode = root;
        foreach (var word in words)
        {
            curNode = root;
            foreach (var c in word)
            {
                if (curNode.nextChar.ContainsKey(c)==false)
                {
                    curNode.nextChar[c] = new TrieNode();
                }
                curNode.nextChar[c].value +=1;
                curNode = curNode.nextChar[c];
            }
            
        }
        int[] ans = new int[words.Length];
        int tempAns=0;
        int theIndex = 0;
        foreach (var word in words)
        {
            
            tempAns = 0;
            curNode = root;
            foreach (var c in word)
            {
                curNode = curNode.nextChar[c];
                tempAns += curNode.value;
            }
            ans[theIndex] = tempAns;
            theIndex+=1;
        }
        return ans;
    }
}