def romanToInt(s):
    n=0
    s=s+'*'
    T = False
    for i in range(0,len(s)):
        if T==True:
            T=False
            continue

        if s[i]=='I':
            if i<len(s):
                if s[i+1]=='V':
                     T = True
                     n=n+4
                     print(n)


                elif  s[i + 1] == 'X':
                    T = True
                    n=n+9
                    print(n)

                else: n = n + 1
                print(n)




        if s[i]=='V':
            n = n + 5
            print(n)

        if s[i]== 'X':
            if i<len(s):
                if s[i+1]=='L':
                     T = True
                     n=n+40
                     print(n)


                elif  s[i + 1] == 'C':
                    T = True
                    n=n+90
                    print(n)




                else: n = n + 10
                print(n)


        if s[i]=='L':
            n = n + 50
            print(n)

        if s[i]=='C':
            if i<len(s):
                if s[i+1]=='D':
                     T = True
                     n=n+400
                     print(n)

                elif  s[i + 1] == 'M':
                    T = True
                    n=n+900
                    print(n)


                else:n = n + 100
                print(n)


        if s[i]=='D':
            n = n + 500
            print(n)


        if s[i]=='M':
            n = n + 1000
            print(n)



    return n





print(romanToInt('MDCCCLXXXIV'))