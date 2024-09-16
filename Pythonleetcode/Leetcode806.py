class Solution(object):
    def numberOfLines(self, widths, S):
        if S=='':
            return [1,0]

        linenum=1
        lastline=0
        for i in range(len(S)):
            if S[i]=='a':
                if lastline+widths[0]<=100:
                    lastline=lastline+widths[0]
                else:
                    lastline=widths[0]
                    linenum=linenum+1
            if S[i]=='b':
                if lastline+widths[1]<=100:
                    lastline=lastline+widths[1]
                else:
                    lastline=widths[1]
                    linenum=linenum+1
            if S[i]=='c':
                if lastline+widths[2]<=100:
                    lastline=lastline+widths[2]
                else:
                    lastline=widths[2]
                    linenum=linenum+1
            if S[i]=='d':
                if lastline+widths[3]<=100:
                    lastline=lastline+widths[3]
                else:
                    lastline=widths[3]
                    linenum=linenum+1
            if S[i]=='e':
                if lastline+widths[4]<=100:
                    lastline=lastline+widths[4]
                else:
                    lastline=widths[4]
                    linenum=linenum+1
            if S[i]=='f':
                if lastline+widths[5]<=100:
                    lastline=lastline+widths[5]
                else:
                    lastline=widths[5]
                    linenum=linenum+1
            if S[i]=='g':
                if lastline+widths[6]<=100:
                    lastline=lastline+widths[6]
                else:
                    lastline=widths[6]
                    linenum=linenum+1
            if S[i]=='h':
                if lastline+widths[7]<=100:
                    lastline=lastline+widths[7]
                else:
                    lastline=widths[7]
                    linenum=linenum+1
            if S[i]=='i':
                if lastline+widths[8]<=100:
                    lastline=lastline+widths[8]
                else:
                    lastline=widths[8]
                    linenum=linenum+1
            if S[i]=='j':
                if lastline+widths[9]<=100:
                    lastline=lastline+widths[9]
                else:
                    lastline=widths[9]
                    linenum=linenum+1
            if S[i]=='k':
                if lastline+widths[10]<=100:
                    lastline=lastline+widths[10]
                else:
                    lastline=widths[10]
                    linenum=linenum+1
            if S[i]=='l':
                if lastline+widths[11]<=100:
                    lastline=lastline+widths[11]
                else:
                    lastline=widths[11]
                    linenum=linenum+1
            if S[i]=='m':
                if lastline+widths[12]<=100:
                    lastline=lastline+widths[12]
                else:
                    lastline=widths[12]
                    linenum=linenum+1
            if S[i]=='n':
                if lastline+widths[13]<=100:
                    lastline=lastline+widths[13]
                else:
                    lastline=widths[13]
                    linenum=linenum+1
            if S[i]=='o':
                if lastline+widths[14]<=100:
                    lastline=lastline+widths[14]
                else:
                    lastline=widths[14]
                    linenum=linenum+1
            if S[i]=='p':
                if lastline+widths[15]<=100:
                    lastline=lastline+widths[15]
                else:
                    lastline=widths[15]
                    linenum=linenum+1
            if S[i]=='q':
                if lastline+widths[16]<=100:
                    lastline=lastline+widths[16]
                else:
                    lastline=widths[16]
                    linenum=linenum+1
            if S[i]=='r':
                if lastline+widths[17]<=100:
                    lastline=lastline+widths[17]
                else:
                    lastline=widths[17]
                    linenum=linenum+1
            if S[i]=='s':
                if lastline+widths[18]<=100:
                    lastline=lastline+widths[18]
                else:
                    lastline=widths[18]
                    linenum=linenum+1
            if S[i]=='t':
                if lastline+widths[19]<=100:
                    lastline=lastline+widths[19]
                else:
                    lastline=widths[19]
                    linenum=linenum+1
            if S[i]=='u':
                if lastline+widths[20]<=100:
                    lastline=lastline+widths[20]
                else:
                    lastline=widths[20]
                    linenum=linenum+1
            if S[i]=='v':
                if lastline+widths[21]<=100:
                    lastline=lastline+widths[21]
                else:
                    lastline=widths[21]
                    linenum=linenum+1
            if S[i]=='w':
                if lastline+widths[22]<=100:
                    lastline=lastline+widths[22]
                else:
                    lastline=widths[22]
                    linenum=linenum+1
            if S[i]=='x':
                if lastline+widths[23]<=100:
                    lastline=lastline+widths[23]
                else:
                    lastline=widths[23]
                    linenum=linenum+1
            if S[i]=='y':
                if lastline+widths[24]<=100:
                    lastline=lastline+widths[24]
                else:
                    lastline=widths[24]
                    linenum=linenum+1
            if S[i]=='z':
                if lastline+widths[25]<=100:
                    lastline=lastline+widths[25]
                else:
                    lastline=widths[25]
                    linenum=linenum+1



        return [linenum,lastline]








print(Solution().numberOfLines([10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10],"abcdefghijklmnopqrstuvwxyz"))
print(Solution().numberOfLines([4,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10],"bbbcccdddaaa"))