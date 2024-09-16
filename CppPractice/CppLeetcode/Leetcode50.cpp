
#include<map>
using namespace std;

class Solution {
private:
    double PowHelper(double x, long n)
    {
        if (n==1)
        {
            return x;
        }
        else if (n==0)
        {
            return 1;
        }
        else 
        {
            double half = PowHelper(x,n/2);
            if (n%2==0)
            {
                return half * half;
            }
            else
            {
                return x * half * half;
            }
        }
        

    }
public:
    double myPow(double x, long n) 
    {

        if(x==1)
        {
            return 1;
        }
        if(n>1)
        {
            return PowHelper(x,n);
        }
        else if(n<1)
        {
            return PowHelper(1/x,-n);
        }
        else if (n==1)
        {
            return x;
        }
        return 0;
    }
};