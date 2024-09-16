public class Solution47{
    Dictionary<int,int> theDict = new Dictionary<int, int>();
    public void helper(List<int> valTemp,int[] nums,IList<IList<int>> result)
    {
        if(valTemp.Count == nums.Length)
        {
            result.Add(new List<int>(valTemp));
            return;
        }
        foreach (var item in theDict)
        {
            if(item.Value!=0)
            {
                theDict[item.Key]--;
                valTemp.Add(item.Key);
                helper(valTemp,nums,result);
                theDict[item.Key]++;
                valTemp.RemoveAt(valTemp.Count-1);
            }
        }
        return;
    }
    public IList<IList<int>> PermuteUnique(int[] nums) 
    {
        IList<IList<int>> result = new List<IList<int>>();
        List<int> temp= new List<int>();
        
        foreach (int num in nums)
        {
            if (!theDict.ContainsKey(num))
            {
                theDict[num] = 1;
            }
            else
            {
                theDict[num]++;
            }
        }
        helper(temp,nums,result);
        return result; 
    }
}