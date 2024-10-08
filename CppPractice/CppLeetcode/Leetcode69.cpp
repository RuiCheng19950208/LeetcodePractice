class Solution {
public:
    int mySqrt(int x) 
    {
        if(x==0){return 0;}
        if(x==1){return 1;}
        long long right = x;
        long long left = 1 ;   
        while(left<right)
        {
            long long mid= (right+left)/2;
            if(mid*mid>x){right=mid-1;}
            else if(mid*mid==x){return mid;}
            else{left=mid+1;}
        }
        if(left*left>x){return left-1;}
        else{return left;}

    }
};