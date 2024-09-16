#include<set>
using namespace std;
class Solution {
public:
    bool isPowerOfTwo(int n) 
    {
        set<int> theSet;
        int kernal = 1;
        theSet.insert(kernal);
        for (int i = 0; i < 32; i++)
        {
            kernal *=2;
            theSet.insert(kernal);
        }

        return theSet.find(n)!=theSet.end();
        
        
    }
};