def isPalindrome(x):
    x=str(x)
    y=x[::-1]
    if x==y:
        return True
    return False


print(isPalindrome(121))
print(isPalindrome(-121))