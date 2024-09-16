class Solution(object):
    def pushDominoes(self, dominoes):
        dominoes_list=[]
        for i in dominoes:
            dominoes_list.append(i)
        # print(dominoes_list)
        pointer=[]
        for i in range(len(dominoes_list)):
            if dominoes_list[i]=="L":
                pointer.append([i,'L'])
            elif dominoes_list[i]=="R":
                pointer.append([i,'R'])
        if len(pointer)==0:
            return dominoes

        if pointer[0][1]=="L":
            for i in range(pointer[0][0]+1):
                dominoes_list[i]="L"
            pointer.pop(0)

        if len(pointer)>0 and pointer[-1][1]=="R":
            for i in range(pointer[-1][0],len(dominoes_list)):
                dominoes_list[i]="R"
            pointer.pop(-1)
        # print(''.join(dominoes_list))


        num_N=0
        while True:
            # print(pointer,dominoes_list)
            for i in range(len(pointer)):
                if pointer[i][1]=="R" and i!=len(pointer)-1 and pointer[i+1][1]=="L" and  pointer[i+1][0]-pointer[i][0]<=2:
                    pointer[i][1] ="N"
                    pointer[i+1][1] = "N"
                    num_N += 2
                elif pointer[i][1]=="R":
                    if pointer[i][0]<len(dominoes_list):
                        if dominoes_list[pointer[i][0]+1]!="R":
                            dominoes_list[pointer[i][0]+1] = "R"
                            pointer[i][0]+=1
                        else:
                            pointer[i][1]="N"
                            num_N += 1

                    else:
                        pointer[i][1] = "N"
                        num_N+=1
                elif pointer[i][1]=="L":
                    if pointer[i][0]>0:
                        if dominoes_list[pointer[i][0] - 1] != "L":
                            dominoes_list[pointer[i][0] - 1] = "L"
                            pointer[i][0]-=1
                        else:
                            pointer[i][1] = "N"
                            num_N += 1
                    else:
                        pointer[i][1] = "N"
                        num_N += 1
            if num_N==len(pointer):
                break


        dominoes=''.join(dominoes_list)
        return dominoes

print(Solution().pushDominoes(".L.R...LR..L.."))
print(Solution().pushDominoes("RR.L"))