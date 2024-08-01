import random
class Randomizedset:
    def __init__(self):
        self.list = []
        self.dict = {}

    def insert(self,val):
        if val not in self.dict:
            self.dict[val] = set()
        self.dict[val].add(len(self.list))
        self.list.append(val)    
        return len(self.dict[val]) == 1

    def remove(self,val):
        if val not in self.dict or not self.dict[val]:
            return False
        index_to_remove  = self.dict[val].pop() 
        last_val = self.list[len(self.list)-1]
        self.list[index_to_remove] = last_val
        if self.dict[last_val]:
            self.dict[last_val].add(index_to_remove)
            self.dict[last_val].discard(len(self.list)-1)
        self.list.pop()
        if not self.dict[val]:
            del self.dict[val]
        return True

    def get_random(self):
        return random.choice(self.list) 

randomset = Randomizedset()   
print(randomset.insert(1))  
print(randomset.insert(3))
print(randomset.insert(1)) 
print(randomset.insert(2)) 
print(randomset.remove(1)) 
print(randomset.remove(2))
print(randomset.get_random()) 

