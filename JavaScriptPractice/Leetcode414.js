var thirdMax = function(nums) {
    let theSet = new Set(nums);
    let theSetArray = Array.from(theSet);
    theSetArray.sort((a, b) => a - b)
    if (theSetArray.length<3) {
        return theSetArray[theSetArray.length-1];
        
    }
    else 
    {
        return theSetArray[theSetArray.length-3];
    }

};