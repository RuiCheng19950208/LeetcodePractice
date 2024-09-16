public class Solution349 {
    public int[] Intersection(int[] nums1, int[] nums2) {
        HashSet<int> set1 = new HashSet<int>(nums1);
        HashSet<int> set2 = new HashSet<int>(nums2);
        List<int> res  =new List<int>();
        foreach (int item in set1)
        {
            if (set2.Contains(item))
            {
                res.Add(item);
            }
            
        }
        return res.ToArray();
        
    }
}