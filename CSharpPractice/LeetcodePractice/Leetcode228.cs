
public class Solution228 {
    public IList<string> SummaryRanges(int[] nums) {
        IList<string> ans = new List<string>();
        string tempString = "";
        int start = 0;
        int end = 0;


        bool isConcatenate = false;
        for(int i=0; i<nums.Length ; i++)
        {
            if(!isConcatenate)
            {
                tempString = nums[i].ToString();
                if(i+1<nums.Length && nums[i+1]-nums[i]==1)
                {
                    start = nums[i] ; 
                    end = nums[i];
                    isConcatenate =true;
                    tempString = start.ToString()+"->"+end.ToString();
                }
                else
                {
                    ans.Add(tempString);
                    isConcatenate = false;
                }
            }
            else
            {
                end = nums[i];
                tempString = start.ToString()+"->"+end.ToString();
                if(!(i+1<nums.Length && nums[i+1]-nums[i]==1))
                {

                    ans.Add(tempString);
                    isConcatenate =false;
                }
            }
        }
        return ans;
    }
}