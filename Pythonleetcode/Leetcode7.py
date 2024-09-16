def reverse( x):
    x=str(x)
    if x[0]=='-':
        a=x[1:]
        a=a[::-1]
        x='-'+a
        if int(x)>=-(2**31) and int(x)<=2**31-1:
            return int(x)
        return 0
    x=x[::-1]

    if int(x) >= -(2 ** 31) and int(x) <= 2 ** 31 - 1:
        return int(x)

    return 0

print(reverse(123))