public class Solution441 {
    public int ArrangeCoins(int n) 
    {
        int left=0;
        int right = n;
        int mid = 0;
        long temp = 0;
        while(left<=right)
        {
            mid = (right+left)/2;
            temp=((long)mid*(mid+1))/2;
            if(temp<n){left=mid+1;}
            else if(temp>n){right=mid-1;}
            else{return mid;}
        }
        return left-1;
    }
}