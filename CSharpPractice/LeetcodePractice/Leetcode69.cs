public class Solution69 {
    public int MySqrt(int x) 
    {
        long left = 1;
        long right = x/2;
        if(x==0 || x==1){return x;}
        long mid = 0;
        long square =0;
        while(left<=right)
        {
            mid = (left+right)/2;
            square = mid*mid;
            if(square<x)
            {
                left = mid+1;
            }
            else if(square>x)
            {
                right = mid-1;
            }
            else{return (int)mid;}
        }
        Console.WriteLine(right);
        if((right+1) * (right+1)<=x){return (int)right+1;}
        else if(right*right>x){return (int)right-1;}
        else{return (int)right;}
        
    }
}