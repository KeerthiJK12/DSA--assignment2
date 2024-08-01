class Queue:
    def __init__(self):
        self.s1 = []
        self.s2 = []
        self.size = 0

    def get_size(self):
        return self.size

    def is_empty(self):
        return self.size == 0

    def push(self,data):
        self.s1.append(data)
        self.size +=1 

    def peek(self):
        if self.size == 0:
            return None
        if not self.s2:
            while self.s1:
                self.s2.append(self.s1.pop())
        return self.s2[-1]    

    def pop(self):
        if self.size == 0:
            return None
        else:
            if not self.s2:
                while self.s1:
                    self.s2.append(self.s1.pop())
            self.size -=1
            return self.s2.pop() 
        
q = Queue()
q.push(1)
q.push(2)
q.push(3)
q.push(4)
q.push(5)
q.push(6)
print(q)
print(q.pop())
print(q.pop())

        







