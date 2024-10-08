var isPerfectSquare = function(num) {
    if (num<2) {
        return true
    }
    let right=num
    let left =2
    let mid = Math.floor((left+right)/2)
    while (left<=right) {
        let cur=mid*mid
        if (cur==num) {
            return true
        }
        else if (cur<num) {
            left = mid+1
            mid = Math.floor((left+right)/2)
        }
        else 
        {
            right = mid-1
            mid = Math.floor((left+right)/2)
        }
    }
    return false
};