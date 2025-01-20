public class Solution58 {
    public int LengthOfLastWord(string s) 
    {
        s= s.Trim();
        string[] sArray = s.Split(" ");
        // foreach (string word in sArray)
        // {
        //     Console.WriteLine(word);
        // }
        return sArray[sArray.Length-1].Length;
    }
}