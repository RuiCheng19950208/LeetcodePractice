def strStr( haystack, needle):
    if  needle=="":
        return 0

    if haystack==needle:
            return 0
    for i in range(0,len(haystack)-len(needle)+1):
        print(haystack[i:i+len(needle)])
        if haystack[i:i+len(needle)]==needle:
            return i
    return -1





print(strStr("hell","ll"))