public class NumArray {

    public List<int> theSumList = new List<int>(0);
    public NumArray(int[] nums) {
        int theSum = 0;
        for (var i = 0; i < nums.Count(); i++)
        {
            theSum +=nums[i];
            theSumList.Add(theSum);   
        }   
    }
    public int SumRange(int left, int right) {
        
        return theSumList[right+1] - theSumList[left];
    }
}
