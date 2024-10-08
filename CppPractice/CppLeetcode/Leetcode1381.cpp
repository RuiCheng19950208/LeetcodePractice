class CustomStack {
public:
    vector<int> theStack;
    int maxSizePublic;
    CustomStack(int maxSize) {
        maxSizePublic = maxSize;
    }
    
    void push(int x) {
        if(theStack.size()<maxSizePublic){theStack.push_back(x);}
        
    }
    
    int pop() {
        if(theStack.size()==0){return -1;}
        else{int ans = theStack.back();theStack.pop_back();return ans;}
    }
    
    void increment(int k, int val) {
        for(int i=0;i<std::min(static_cast<size_t>(k),theStack.size());i++)
        {
            theStack[i]+=val;
        }
        
    }
};
