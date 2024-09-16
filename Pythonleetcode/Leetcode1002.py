class Solution(object):
    def commonChars(self, A):
        ans=[]
        temp_list_dict = []
        for i in A:
            temp_dict={}
            for c in i:
                if c not in temp_dict.keys():
                    temp_dict[c]=1
                else:
                    temp_dict[c] += 1
            temp_list_dict.append(temp_dict)
            # print(temp_dict)


        temp_dict=temp_list_dict[0]
        for dict in temp_list_dict:
            for key in dict.keys():
                for key_temp in list(temp_dict.keys()):
                    if key_temp not in list(dict.keys()):
                        # print(key_temp,list(dict.keys()))
                        del temp_dict[key_temp]
                if key not in  temp_dict.keys():
                    continue
                else:
                    temp_dict[key]=min(temp_dict[key],dict[key])
        ans=[]
        for key in temp_dict:
            for value in range(temp_dict[key]):
                ans.append(key)

        return ans
print(Solution().commonChars( ["bella","label","roller"]))
print(Solution().commonChars(["cool","lock","cook"]))
