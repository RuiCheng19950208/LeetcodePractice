class MinStack(object):

    def __init__(self):
        self.mystack=[]


    def push(self, val):
        self.mystack.append(val)


    def pop(self):
        self.mystack.pop()


    def top(self):
        return self.mystack[-1]


    def getMin(self):
        return min(self.mystack)
