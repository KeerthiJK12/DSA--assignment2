import random
class Randomizedset:
    def __init__(self):
        self.list = []
        self.map_list = {}

    def insert(self,val):
        if val in self.map_list:
            return False 
        else:
            self.list.append(val)
            self.map_list[val] = len(self.list)-1
        return True  

    def remove(self,val):
        if val not in self.map_list:
            return False
        else:
            index = self.map_list[val]  
            last_value = self.list[len(self.list)-1]  
            self.list[index] = last_value
            self.map_list[last_value] = index
            self.list.pop()
            del self.map_list[val]  
        return True

    def get_random(self):
        return random.choice(self.list)#always takes list,tuple or string as an argument


randomset = Randomizedset()
print (randomset.insert(3))
print (randomset.insert(4))
print (randomset.remove(2))
print (randomset.insert(4))
print (randomset.remove(3))
print(randomset.get_random())

