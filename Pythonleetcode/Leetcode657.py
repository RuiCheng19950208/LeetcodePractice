
def judgeCircle(moves):
        orix = 0
        oriy = 0
        tracex = []
        tracey = []
        tracex.append(orix)
        tracey.append(oriy)
        for i in range(0,len(moves)):
            if moves[i]=="L":
                orix=orix-1
                tracex.append(orix)
                tracey.append(oriy)

            elif moves[i]=="R":
                orix=orix+1
                tracex.append(orix)
                tracey.append(oriy)

            elif moves[i]=="U":
                oriy=oriy+1
                tracex.append(orix)
                tracey.append(oriy)

            elif moves[i]=="D":
                oriy=oriy-1
                tracex.append(orix)
                tracey.append(oriy)


        k=len(tracex)
        if tracex[0]==tracex[k-1] and tracey[0]==tracey[k-1]:
            return True

        return False


print(judgeCircle("UD"))
