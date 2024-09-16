var threeSum = function(nums) 
{
    let res=[]
    let left = 0
    let right = 0
    let lenN = nums.length
    let theSum = 0
    nums.sort((a, b) => a - b)
    for (let i = 0; i < lenN; i++) {
        if (i>0 && nums[i]==nums[i-1]) {
            continue
        }
        left = i+1
        right = lenN-1
        while (left<right) {
            theSum = nums[i]+nums[left]+nums[right]
            if (theSum==0) {
                let temp=[nums[i],nums[left],nums[right]]
                res.push(temp)
                left++
                while (left<right && nums[left]==nums[left-1]) {
                    left++
                }
                right--
                while (left<right && nums[right]==nums[right+1]) {
                    right--
                }
            }
            else if(theSum<0) 
            {
                left++
                while (left<right && nums[left]==nums[left-1]) {
                    left++
                }
                
            }
            else 
            {
                right--
                while (left<right && nums[right]==nums[right+1]) {
                    right--
                }
            }
        }
    }
    return res
};