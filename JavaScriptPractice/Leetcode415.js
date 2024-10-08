var addStrings = function(num1, num2) {
    let ptr1 = num1.length-1;
    let ptr2 = num2.length-1;
    let carry=0;
    let ans="";

    while (ptr1>=0||ptr2>=0||carry>0) {
        let d1=0;
        let d2=0;
        if (ptr1>=0) {
            d1 = num1[ptr1--]-'0';
        }
        if (ptr2>=0) {
            d2 = num2[ptr2--]-'0';
        }
        let theSum = d1+d2+carry;
        ans += theSum%10;
        carry = Math.floor(theSum/10);
    }

    ans = ans.split("").reverse().join("");
    return ans;
    
};