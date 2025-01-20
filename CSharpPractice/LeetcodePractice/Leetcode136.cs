public class Solution136 {
    public int SingleNumber(int[] nums) 
    {
        Dictionary<int,int> map = new Dictionary<int,int>();
        foreach(int num in nums)
        {
            if(!map.ContainsKey(num)){map[num]=1;}
            else{map[num]++;}
        }
        foreach(KeyValuePair<int, int> pair in map)
        {
            if(pair.Value ==1){return pair.Key;}
        }
        return -1;
    }
}