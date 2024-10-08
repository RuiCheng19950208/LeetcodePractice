function reverse(nums,left,right)
{
    while(left<right)
    {
        let temp= nums[left];
        nums[left] = nums[right];
        nums[right] = temp;
        left++;
        right--;
    }
    return;

};
var rotate = function(nums, k) 
{   
    let n = nums.length;
    k = k%n;
    reverse(nums,0,n-1);
    reverse(nums,0,k-1);
    reverse(nums,k,n-1);
    return;
};