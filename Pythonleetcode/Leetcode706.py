class MyHashMap(object):

    def __init__(self):
        self.keys=[]
        self.values=[]

    def put(self, key, value):
        """
        value will always be non-negative.
        :type key: int
        :type value: int
        :rtype: None
        """
        key_exist = False
        for i in range(len(self.keys)):
            if self.keys[i]==key:
                key_exist=True
                self.values[i]=value
        if key_exist==False:
            self.keys.append(key)
            self.values.append(value)


    def get(self, key):
        """
        Returns the value to which the specified key is mapped, or -1 if this map contains no mapping for the key
        :type key: int
        :rtype: int
        """
        for i in range(len(self.keys)):
            if self.keys[i]==key:
                return self.values[i]
        return -1

    def remove(self, key):
        """
        Removes the mapping of the specified value key if this map contains a mapping for the key
        :type key: int
        :rtype: None
        """
        if key not in self.keys:
            # print("wrong",key,self.keys)
            return
        for i in range(len(self.keys)):
            if self.keys[i]==key:
                self.keys.pop(i)
                self.values.pop(i)
                return


hashMap = MyHashMap()
hashMap.put(1, 1)
hashMap.put(2, 2)
print(hashMap.get(1))
print(hashMap.get(3))
hashMap.put(2, 1)
print(hashMap.get(2))
hashMap.remove(2)
print(hashMap.get(2))

# Your MyHashMap object will be instantiated and called as such:
# obj = MyHashMap()
# obj.put(key,value)
# param_2 = obj.get(key)
# obj.remove(key)