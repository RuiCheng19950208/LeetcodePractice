class Solution(object):
    def convert(self, s, numRows):
        """
        :type s: str
        :type numRows: int
        :rtype: str
        """
        if numRows==1:
            return s
        result_array=[]
        backward_index=0
        for i in range(numRows):
            result_array.append([])

        dividor=(2 * numRows - 2)

        for i in range(len(s)):
            key_index=i % dividor
            if key_index>=numRows:
                backward_index=1
            else:
                backward_index=0
            if backward_index==0:
                result_array[key_index].append(s[i])
            else:
                for j in range(numRows):
                    if dividor==j+(key_index):
                        result_array[j].append(s[i])
                    else:
                        result_array[j].append('')
        # print(result_array)
        result=''
        for i in range(numRows):
            result +=''.join(x for x in result_array[i])
        return result












print(Solution().convert( s = "PAYPALISHIRING", numRows = 3))
print(Solution().convert( s = "PAYPALISHIRING", numRows = 4))