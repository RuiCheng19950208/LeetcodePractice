#include<vector>
#include <algorithm>

using namespace std;

class Solution {
public:
    bool isPalindrome(int x) {
        int remainder = x;
        vector<int> numList;
        vector<int> reversedNumList;
        if (x<0)
        {
            return false;
        }
        
        
        while (remainder>0)
        {
            numList.push_back(remainder%10);
            remainder = remainder/10;
        }
        reversedNumList = numList;
        reverse(reversedNumList.begin(),reversedNumList.end());
        return (numList==reversedNumList);

        
    }
};