class Stack:
    def __init__(self):
        self.q1 = []
        self.q2 = []
        self.size = 0

    def get_size(self):
        return self.size 

    def push(self,data):
        self.q1.append(data)
        self.size +=1

    def pop(self):
        if len(self.q1)>1:
            self.q2.append(self.q1.pop(0))   
        ret = self.q1.pop()
        self.q1,self.q2 = self.q2,self.q1
        self.size-=1   
        return ret

s = Stack()
s.push(1)
s.push(2)
s.push(7)
s.push(9)
s.push(4)
s.push(6)   

popped_element = s.pop()
print(popped_element) 
                             