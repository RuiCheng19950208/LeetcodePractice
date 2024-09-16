var spiralOrder = function(matrix) 
{
    let m =matrix.length;
    let n= matrix[0].length;
    let step = m*n;
    let directions = [[0,1],[1,0],[0,-1],[-1,0]]
    let directIndex = 0
    let curRow =0;
    let curCol = 0;
    let visited = Array.from({length:m},()=>Array(n).fill(false))
    let res = []
    while (step>0) {
        res.push(matrix[curRow][curCol])
        visited[curRow][curCol]=true
        step--
        let nextRow = curRow+ directions[directIndex][0];
        let nextCol = curCol+ directions[directIndex][1];
        if (nextRow<0||nextCol<0||nextRow>m-1||nextCol>n-1||visited[nextRow][nextCol]==true) {
            directIndex =(directIndex+1)%4
            
        }
        curRow = curRow+ directions[directIndex][0];
        curCol = curCol+ directions[directIndex][1];
    }
    return res
};