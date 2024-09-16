public class Solution46 {

    public void PermuteHelper(int[] nums, List<int> temp, IList<IList<int>> result) 
    {
        if (temp.Count == nums.Length)
        {
            result.Add(new List<int>(temp));
            return;
        }
        for (int i = 0; i < nums.Length; i++)
        {
            if (temp.Contains(nums[i]))
            {
                continue;
            }
            temp.Add(nums[i]);
            PermuteHelper(nums, temp, result);
            temp.Remove(nums[i]); 
        }
    }
    public IList<IList<int>> Permute(int[] nums) 
    {
        IList<IList<int>> result = new List<IList<int>>();
        List<int> temp =new List<int>();
        PermuteHelper(nums, temp, result);
        return result;
        
    }
}