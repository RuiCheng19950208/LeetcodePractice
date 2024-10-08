class Solution {
public:
    int countSegments(string s) {
        bool isCount = true;
        int ans=0;
        for(int i = 0; i < s.size(); i++)
        {
            if (s[i]==" ")
            {
                isCount=true;
            }
            else if (s[i]!=" " && isCount==true)
            {
                ans++;
                isCount =false;
            }
        }
        return ans;
    }
};