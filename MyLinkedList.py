class Node:
    def __init__(self,data,next = None):
        self.data = data
        self.next = next

class Mylinkedlist:
    def __init__(self):
        self.head = None
        self.tail = None 
        self.size = 0      

    def get(self,index):
        if index < 0 or index >= self.size:
            return -1
        else:
            curr = self.head
            for i in range(index):
                curr = curr.next
            return curr.data

    def addAtHead(self,data):
        newnode = Node(data)
        if not self.head:
            self.head = newnode
            self.tail = newnode
        else:
            temp = newnode
            temp.next = self.head
            self.head = temp  
        self.size +=1  

    def addAtTail(self,data):
        newnode = Node(data)
        if not self.head:
            self.head = newnode
            self.tail = newnode
        else:
            self.tail.next = newnode
            self.tail = newnode
        self.size +=1

    def addAtIndex(self,index,data):
        if index < 0 or index > self.size:
            return "Invalid index"
        if index == 0:
            self.addAtHead(data)  
        elif index == self.size:
            self.addAtTail(data)
        else:
            newnode = Node(data)
            curr = self.head
            for i in range(index-1):
                curr = curr.next
            newnode.next = curr.next
            curr.next = newnode  
            self.size +=1

    def removeAtIndex(self,index):
        if index <0 or index >= self.size:
            return "Invalid Index"

        if index == 0:
            temp = self.head
            self.head = temp.next
        else:
            trav = self.head
            for i in range(index - 1):
                trav = trav.next
            temp = trav.next
            trav.next = temp.next
            if index == self.size-1:
                self.tail = trav
        del temp
        self.size -= 1    

    def __str__(self):
        if not self.head:
            return "None"
        curr = self.head
        result = []
        while curr:
            result.append(curr.data)
            curr = curr.next
        return "->".join(map(str,result)) + "->None"   
      

ll = Mylinkedlist()
ll.addAtIndex(0,4)
ll.addAtHead(3)
ll.addAtIndex(2,8)
ll.removeAtIndex(1)
print(ll)







            


           


            









