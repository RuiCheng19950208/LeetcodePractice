public class Solution1590 {
    public int MinSubarray(int[] nums, int p) {

        long goal = nums.Select(num=>(long)(num%p)).Sum()%p;
        if(goal==0){return 0;}
        Dictionary<int,int> theDict =new Dictionary<int,int>{{0,-1}};
        int n = nums.Length;
        int ans = n,cur=0,target=0;
        for(int i=0;i<n;i++)
        { 
            cur=(cur+nums[i])%p;
            target = (cur+p-(int)goal)%p;
            if(theDict.ContainsKey(target))
            {
                ans=Math.Min(ans,i-theDict[target]);
            }
            theDict[cur] = i;
        }
        return ans==n?-1:ans;
    }
}