public class Solution128 {
    public int LongestConsecutive(int[] nums) 
    {
        int ans=1;
        int temp=1;
        HashSet<int> theSet = new HashSet<int>(nums);
        List<int> theList = theSet.ToList();
        theList.Sort();
        if(theList.Count==0){return 0;}
        if(theList.Count==1){return 1;}
        for(int i=1;i<theList.Count;i++)
        {
            if(theList[i]-theList[i-1]==1)
            {
                temp+=1;
                ans=Math.Max(ans,temp);
            }
            else{temp=1;}
        }
        return ans;
        
    }
}