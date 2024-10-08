public class Solution414 {
    public int ThirdMax(int[] nums) {
        HashSet<int> theSet = new HashSet<int>(nums);
        List<int> theSetList = new List<int>(theSet);
        theSetList.Sort();
        if (theSetList.Count<3)
        {
            return theSetList[theSetList.Count-1];
        }
        else
        {
            return theSetList[theSetList.Count-3];
        }
        
        
    }
}