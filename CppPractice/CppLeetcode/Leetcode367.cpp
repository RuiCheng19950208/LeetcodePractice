class Solution {
public:
    bool isPerfectSquare(int num) {
        if (num<2)
        {
            return true;
        }
        long left =2;
        long right = num;
        long mid = (left+right)/2;
        while (left<=right)
        {
            long cur = mid*mid;
            if (cur==num)
            {
                return true;
            }
            else if (cur<num)
            {
                left = mid+1;
                mid = (left+right)/2;
            }
            else
            {
                right = mid-1;
                mid = (left+right)/2;
            }
        }
        return false;
    }
};