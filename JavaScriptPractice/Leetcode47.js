var theDict;
var result;
var temp;
var numsLen;

function helper()
{
    if (temp.length == numsLen) 
    {
        result.push([...temp]);
        return;   
    }
    for(let key in theDict)
    {
        if (theDict[key]!=0) 
        {
            theDict[key]--;
            temp.push(key);
            helper();
            theDict[key]++;  
            temp.pop();
        }
    }

    return;
}

var permuteUnique = function(nums) 
{
    theDict = {};
    result = [];
    temp=[];
    numsLen = nums.length;
    for (let i = 0; i < nums.length; i++) {
        if (!(nums[i] in theDict)) {
            theDict[nums[i]] = 1;
        }
        else
        {
            theDict[nums[i]]++;
        }
    }
    console.log(theDict);
    helper();
    return result;
    
};