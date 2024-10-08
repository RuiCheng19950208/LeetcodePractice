public class Solution2696 {
    public int MinLength(string s) 
    {
        Stack<char> theStack = new Stack<char>();
        for(int i=0;i<s.Length;i++)
        {
            if(theStack.Count>0)
            {
                char lastElement = theStack.Peek();
                if((s[i]=='B'&&lastElement=='A')||(s[i]=='D'&&lastElement=='C'))
                {
                    theStack.Pop();
                }
                else
                {
                    theStack.Push(s[i]);
                }

            }
            else
            {
                theStack.Push(s[i]);
            }
        }
        return theStack.Count;
        
    }
}