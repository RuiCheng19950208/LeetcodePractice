#include <set>
#include <string>
#include <vector>
using namespace std;

class Solution {
public:
    
    int countConsistentStrings(string allowed, vector<string>& words) 
    {
        set<char> goalSet;
        int ans = 0;
        for(char c:allowed)
        {
            goalSet.insert(c);
        }
        for(string word:words)
        {
            set<char> tempSet;
            bool isSubset = true;
            for(char c:word)
            {
                tempSet.insert(c);
            }
            for(char c:tempSet)
            {
                if(goalSet.find(c)==goalSet.end())
                {
                    isSubset = false;
                    break;
                }
            }
            if(isSubset)
            {
                ans++;
            }
        }
        return ans;
    }
};