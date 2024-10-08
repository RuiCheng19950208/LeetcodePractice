var theSumList=[0]
var NumArray = function(nums) 
{   
    let theSum = 0;
    for (let i = 0; i < nums.length; i++) {
        theSum += nums[i]
        theSumList.push(theSum)
    }

};

NumArray.prototype.sumRange = function(left, right) 
{
    return theSumList[right+1]-theSumList[left]
};