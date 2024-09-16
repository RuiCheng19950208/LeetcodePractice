var construct2DArray = function(original, m, n) 
{
    let result=[];
    let count=0;
    for (let i = 0; i < m; i++) {
        let row=[];
        for (let j = 0; j < n; j++) {
            row.push(original[count]);
            count++;
            
        }
        result.push(row);
        
    }
    return result;
    
};