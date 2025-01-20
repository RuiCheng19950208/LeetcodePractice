public class Solution2683 {
    public bool DoesValidArrayExist(int[] derived) 
    {
        int signal = derived.Sum();
        int n = derived.Length;
        signal -= derived[n-1];
        if(signal %2==1){return derived[n-1]==1;}
        else{return derived[n-1]==0;}
    }
}