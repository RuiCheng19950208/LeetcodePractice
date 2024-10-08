var isSolved
function isValid(row,col,c,board)
{   console.log(c,row,col)
    for (let i = 1; i <=9; i++) {
        
        if (board[i][col]==c || board[row][i]==c || board[Math.floor(row/3)+Math.floor(i/3)][Math.floor(col/3)+Math.floor(i%3)]==c) 
        {
            return false
        }
       
    }
    return true


};
function dfs(row,col,board)
{
    if (row==9) {
        isSolved = true
        return
    }
    if (col==9)
    {
        dfs(row+1,0,board)
        return
    }
    if (board[row][col]!='.') {
        dfs(row,col+1,board)
        return
        
    }
    else{
        for (let i = 1; i <= 9; i++) {
            let c = (i+1).toString()
            if (isValid(row,col,c,board)) 
            {
                board[row][col] = c
                dfs(row,col+1,board)
                if (isSolved) {
                    return
                }
                board[row][col] ='.'
            }
        }
    }
    return
};

var solveSudoku = function(board) {
    isSolved = false
    dfs(0,0,board)
    return
};