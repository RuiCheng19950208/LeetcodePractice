class Solution {
public:
    void bubble(vector<int> &nums)
    {
        int n =nums.size();
        for(int i=0;i<n-1;i++)
        {
            for(int j=0;j<n-1-i;j++)
            {
                if(nums[j]>nums[j+1]){swap(nums[j],nums[j+1]);}
            }
        }
        return;
    }
    void selection(vector<int> &nums)
    {
        int n =nums.size();
        for(int i=0;i<n;i++)
        {
            int maxIndex = 0;
            for(int j=0;j<=n-i-1;j++)
            {
                if(nums[j]>nums[maxIndex]){maxIndex=j;}

            }
            swap(nums[n-i-1],nums[maxIndex]);
        }
        return;
    }

    void insertion(vector<int> &nums)
    {
        int n= nums.size();
        for(int i=1;i<n;i++)
        {
            int key = nums[i];
            int j = i-1;
            while(j>=0 && nums[j]>key)
            {
                nums[j+1]=nums[j];
                j--;
            }
            nums[j+1]=key;
        }
        return;
    }
    void mergeMerger(vector<int> &nums,int left,int right,int mid)
    {
        int n1 = mid-left+1;
        int n2 = right-mid;
        vector<int> v1,v2;
        for(int i=0;i<n1;i++){v1.push_back(nums[left+i]);}
        for(int i=0;i<n2;i++){v2.push_back(nums[left+n1+i]);}
        int i1=0,i2=0,i3=left;
        while(i1<n1 && i2<n2)
        {
            if(v1[i1]<v2[i2]){nums[i3++]=v1[i1++];}
            else{nums[i3++]=v2[i2++];}
        }
        while(i1<n1){nums[i3++]=v1[i1++];}
        while(i2<n2){nums[i3++]=v2[i2++];}
        return;
    }

    void mergeSpliter(vector<int> &nums,int left,int right)
    {
        if(left<right)
        {
            int mid = left +(right-left)/2;
            mergeSpliter(nums,left,mid);
            mergeSpliter(nums,mid+1,right);
            mergeMerger(nums,left,right,mid);
        }
        return;
    }

    void merge(vector<int> &nums)
    {
        mergeSpliter(nums,0,nums.size()-1);
        return;
    }

    int quickSort(vector<int> &nums,int left,int right)
    {
        int slow=left-1;
        int key = nums[right];
        for(int i=left;i<right;i++)
        {
            if(nums[i]<key)
            {
                slow++;
                swap(nums[i],nums[slow]);
            }
        }
        slow++;
        swap(nums[slow],nums[right]);
        return slow;

    }
    void quickSplit(vector<int>&nums,int left,int right)
    {
        if(left<right)
        {
            int pivotIndex = quickSort(nums,left,right);
            quickSplit(nums,left,pivotIndex-1);
            quickSplit(nums,pivotIndex+1,right);
        }
        
        return;

    }

    void quick(vector<int> &nums)
    {
        quickSplit(nums,0,nums.size()-1);
        return;
    }
    
    int nPublic;
    void heapify(vector<int> &nums,int rootIndex,int size) //Create max heap
    {
        int left = 2*rootIndex+1;
        int right = 2*rootIndex+2;
        int maxIndex = rootIndex;
        if(left<size && nums[left]>nums[maxIndex]){maxIndex = left;}
        if(right<size && nums[right]>nums[maxIndex]){maxIndex = right;}
        if(maxIndex!=rootIndex)
        {
            swap(nums[rootIndex],nums[maxIndex]);
            heapify(nums,maxIndex,size);
        }
        return;


    }
    void heap(vector<int> &nums)
    {
        nPublic = nums.size();
        for(int i=nPublic-1;i>=0;i--)
        {
            heapify(nums,i,nPublic);
        
        }
        for(int i=nPublic-1;i>=0;i--)
        {
            swap(nums[0],nums[i]);
            heapify(nums,0,i);
            
        }
        return;
    }

    void sortColors(vector<int>& nums) 
    {
        // bubble(nums);
        // selection(nums);
        // insertion(nums);

        // merge(nums);
        // quick(nums);
        heap(nums);
        return;
    }
};