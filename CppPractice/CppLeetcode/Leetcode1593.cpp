class Solution {
public:
    string publicS;
    int n;
    unordered_set<string> theSet;
    int helper(int start)
    {
        if(start==n){return theSet.size();}
        int ans=0;
        for(int end=start+1;end<n+1;end++)
        {
            string curString = publicS.substr(start,end-start);
            if(theSet.find(curString)==theSet.end())
            {
                theSet.insert(curString);
                ans = max(ans,helper(end));
                theSet.erase(curString);
            }
            
        }
        return ans;
    }
    int maxUniqueSplit(string s) 
    {
        publicS=s;
        n=s.size();
        return helper(0);
    }
};