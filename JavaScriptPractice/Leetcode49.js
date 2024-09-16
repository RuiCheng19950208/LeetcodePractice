var groupAnagrams = function(strs) 
{
    theDict = []
    result = []
    for(let s of strs)
    {
        let template = s.split('').sorted().join('');
        if (template in Object.keys(theDict)) {
            theDict[template].push(s);
        }
        else{
            theDict[template] = [s];
        }

    }
    for(let key of Object.keys(theDict))
    {
        result.push(theDict[key]);
    }

    
};