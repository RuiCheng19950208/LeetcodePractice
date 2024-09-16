def countAndSay(n):
    if n==1:
        return 1
    c =str(countAndSay(n-1))+'*'
    count=1
    s=''
    for i in range(0,len(c)-1):
        if c[i]==c[i+1]:
            count=count+1
        else :
            s=s+str(count)+str(c[i])
            count=1

    return s


print(countAndSay(10))