class Solution(object):
    def mostCommonWord(self, paragraph, banned):
        list1=[]
        listout=[]
        paragraph=paragraph.lower()
        for i in paragraph:
            if (not i.isalpha()) and ( i!=' '):
                paragraph=paragraph.replace(i,' ')
        list1=paragraph.split()
        a=len(list1)
        k=0
        while(k<a):
            if list1[k] in banned:
                list1.pop(k)
                a=a-1
            k=k+1
        ans=0
        ss=''
        list2=list(set(list1))
        for i in list2:
            if list1.count(i)>ans:
                ans=list1.count(i)
                ss=i
        return ss







print(Solution().mostCommonWord("Bob hit a ball, the hit BALL flew far after it was hit.",["hit"]))
print(Solution().mostCommonWord("Bob!",["hit"]))
print(Solution().mostCommonWord("Bob!",[]))
