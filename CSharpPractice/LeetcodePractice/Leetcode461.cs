public class Solution461 {
    public int HammingDistance(int x, int y) 
    {
        int temp=x^y;
        int ans=0;
        while(temp>0)
        {
            if(temp%2==1){ans++;}
            temp = temp>>1;
        }
        return ans;
    }
}