var isValidSudoku = function(board) 
{
    let colDic = {}
    let rowDic = {}
    let boxIndexDic = {}
    for (let i = 0; i < board.length; i++) {
        for (let j = 0; j < board[0].length; j++) {
            if (board[i][j]!='.') {
                let theVal = board[i][j]-'0'
                let boardIndex = 3*Math.floor(i/3)+Math.floor(j/3)
                if (!colDic[j]) {
                    colDic[j] = new Set()
                
                }
                if (!rowDic[i]) {
                    rowDic[i] = new Set()
                }
                if (!boxIndexDic[boxIndexDic]) {
                    boxIndexDic[boardIndex] = new Set()
                }
                let isPass = !colDic[j].has(theVal)&& !rowDic[i].has(theVal) && !boxIndexDic[boardIndex].has(theVal)
                if(!isPass){return false}
                colDic[j].Add(theVal)
                rowDic[i].Add(theVal)
                boxIndexDic[boardIndex].Add(theVal)
            }
        }
    }
    return true
};