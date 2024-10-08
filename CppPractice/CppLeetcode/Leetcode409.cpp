class Solution {
public:
    int longestPalindrome(string s) {
        map<char,int> theMap;
        bool isPlus=false;
        int ans = 0;
        for(char c:s)
        {
            if (theMap.find(c)==theMap.end())
            {
                theMap[c] = 1;
            }
            else
            {
                theMap[c] += 1;
            }
        }
        for(auto pair:theMap)
        {
            if (pair.second%2==1)
            {
                isPlus=true;
            }
            ans +=2*(pair.second/2);
        }
        if (isPlus)
        {
            ans++;
        }
        return ans;
        
    }
};