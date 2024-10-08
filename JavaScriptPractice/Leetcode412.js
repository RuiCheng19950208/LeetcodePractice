

var fizzBuzz = function(n) {
    let isBuzz=false;
    let isFizz=false;
    let ans=[];
    for (let i = 1; i < n+1; i++) {
        isBuzz=false;
        isFizz=false;
        let temp=i.toString();
        if (i%3==0) {
            isFizz=true;
        }
        if (i%5==0) {
            isBuzz=true;
        }
        if (isFizz && isBuzz) {
            temp="FizzBuzz"
        }
        else if (isFizz) {
            temp="Fizz"
        }
        else if (isBuzz) {
            temp="Buzz"
        }
        ans.push(temp);
        
    }
    return ans;
};