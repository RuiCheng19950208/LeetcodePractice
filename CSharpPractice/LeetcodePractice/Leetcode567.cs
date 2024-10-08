public class Solution567 {
    private bool dictEqual(Dictionary<char,int> d1, Dictionary<char,int> d2)
    {
        foreach(var pair in d1)
        {
            if(pair.Value != d2[pair.Key]){return false;}
            
        }
        return true;

    }
    public bool CheckInclusion(string s1, string s2) 
    {
        int s1len = s1.Length;
        int s2len = s2.Length;
        if(s1len>s2len){return false;}
        Dictionary<char,int> s1Map = new Dictionary<char,int>();
        for(char c='a';c<='z';c++){s1Map[c]=0;}
        foreach(char c in s1){s1Map[c]++;}
        Dictionary<char,int> tempMap = new Dictionary<char,int>();
        for(char c='a';c<='z';c++){tempMap[c]=0;}
        foreach(char c in s2.Substring(0,s1len)){tempMap[c]++;}
        
        int slow = 0;
        int fast=s1len-1;

        for(int i=0;i<s2len-s1len;i++)
        {
            foreach(var kvp in tempMap){Console.WriteLine($"{kvp.Key},{kvp.Value}");}
            if(dictEqual(s1Map,tempMap)){return true;}
            fast++;
            if(fast<=s2len-1)
            {
                tempMap[s2[fast]]++;
                tempMap[s2[slow]]--;
                slow++;
            }
        }
        if(dictEqual(s1Map,tempMap)){return true;}else{return false;}
    }
}