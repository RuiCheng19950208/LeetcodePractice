class Solution {
public:
    int arrangeCoins(int n) 
    {
        int right=n;
        int left=0;
        int mid =0;
        long long temp = 0;
        while(left<=right)
        {
            mid = (right+left)/2;
            temp = (long long)mid * (mid + 1) / 2;
            if(temp<n){left=mid+1;}
            else if(temp>n){right=mid-1;}
            else{return mid;}
        }
        return left-1;
    }
};