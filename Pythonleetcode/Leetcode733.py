class Solution(object):
    def floodFill(self, image, sr, sc, newColor):
        start_coor=[sr,sc]
        coor=[start_coor]
        added_coor = [start_coor]
        target_color=image[sr][sc]
        four_dirc=[[0,1],[0,-1],[1,0],[-1,0]]

        while True:
            previous_len=len(coor)
            temp=[]

            for i in added_coor:
                for j in range(4):
                    k=[min(max(i[0]+four_dirc[j][0],0),len(image)-1),min(max(i[1]+four_dirc[j][1],0),len(image[0])-1)]
                    print(k)
                    if k not in coor and image[k[0]][k[1]]==target_color:
                        coor.append(k)
                        temp.append(k)
            added_coor=temp
            print(previous_len)
            if len(coor)==previous_len:
                break
        for i in coor:
            image[i[0]][i[1]]=newColor

        return image

print(Solution().floodFill(image = [[1,1,1],[1,1,0],[1,0,1]],sr = 1, sc = 1, newColor = 2))