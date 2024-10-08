class Solution {
public:
    int romanToInt(string s) {
        map<char,int> theMap = {{'I',1},{'V',5},{'X',10},{'L',50},{'C',100},{'D',500},{'M',1000}};
        int ans=0;
        for(int i=0;i<s.size();i++)
        {
            if(i!=s.size()-1 && theMap[s[i+1]]>theMap[s[i]]){ans-=theMap[s[i]];}
            else{ans+=theMap[s[i]];}

        }
        return ans;
        
    }
};