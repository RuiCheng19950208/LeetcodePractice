class Solution {
public:
    bool checkInclusion(string s1, string s2) 
    {
        unordered_map<char,int> s1Map;
        int s1len = s1.size();
        int s2len = s2.size();
        for (char c='a';c<='z'+1;c++){s1Map[c] =0;}
        for(char c:s1){s1Map[c]++;}
        unordered_map<char,int> tempMap;
        for (char c='a';c<='z'+1;c++){tempMap[c] =0;}
        for(char c:s2.substr(0,s1len)){tempMap[c]++;}
        int slow = 0;
        int fast = s1len-1;
        for(int i=0;i<s2len-s1len;i++)
        {
            if(tempMap==s1Map){return true;}
            tempMap[s2[slow]]--;
            slow++;
            fast++;
            if(fast<=s2len-1){tempMap[s2[fast]]++;}
        }
        if(tempMap==s1Map){return true;}else{return false;}
    }
};