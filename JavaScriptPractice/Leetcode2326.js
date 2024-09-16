var result;
var curPos;
var directions;
var direcIndex;
var publicm;
var publicn;
function MoveToNext(val)
{
    const curRow = curPos[0];
    const curCol = curPos[1];
    let nextRow = curPos[0] + directions[direcIndex][0];
    let nextCol = curPos[1] + directions[direcIndex][1];
    

    if (nextRow<0 || nextRow>publicm-1 ||nextCol<0 || nextCol>publicn-1 || result[nextRow][nextCol]!=-1) {
        direcIndex = (direcIndex+1)%4;
        nextRow = curPos[0] + directions[direcIndex][0];
        nextCol = curPos[1] + directions[direcIndex][1];
    }
    console.log(val,curPos,nextRow,nextCol);
    curPos = [nextRow,nextCol];
    
    result[curRow][curCol] = val;
    
}

function Create2DArrayAndFillVal(x,y,val)
{
    const ans=[]
    for (let i = 0; i < x; i++) {
        let row = []
        for (let j = 0; j < y; j++) {
            row.push(val);
        }
        ans.push(row)
    }
    return ans;
}

var spiralMatrix = function(m, n, head) 
{
    curPos = [0,0];
    directions = [[0,1],[1,0],[0,-1],[-1,0]];
    direcIndex = 0;
    result = Create2DArrayAndFillVal(m,n,-1);
    
    publicm = m;
    publicn = n;
   
    while (head!=undefined) {
        MoveToNext(head.val);
        head = head.next;
    }

    return result;
    
};