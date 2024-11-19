class circular:
    def __init__(self,s):
        self.size=s
        self.l=[0 for i in range(s)]
        self.rear=-1
        self.front=-1
    def insert(self,item):
        if self.front==(self.rear+1)%self.size:
            print("circular queue is full")
            return
        self.rear=(self.rear+1)% self.size
        self.l[self.rear]=item
        print(item,"insert in queue")
        if self.front==-1:
            self.front=0
    def delete(self):
        if self.front==-1 and self.rear==-1:
            print("circular queue is empty")
            return 
        item=self.l[self.front]
        if self.front==self.rear:
            self.front=-1
            self.rear=-1
            return item
        else:
            self.front=(self.front+1)%self.size    
            return item
    def disp(self):
        if self.front==-1 and self.rear==-1:
            print("circular queue is empty")
        elif self.front<=self.rear:
             for i in range(self.front,self.rear+1):
                print(self.l[i],end=" ")
        else:
            for i in range(self.front,self.size):
                print(self.l[i],end=" ")
            for i in range(0,self.rear+1):
                print(self.l[i],end=" ")
            
        
r1=circular(4)
r1.insert(12)
r1.insert(34)
r1.insert(45)
r1.insert(85)
r1.insert(345)
r1.disp() 
print()
print("deleted element:",r1.delete())
print("deleted element:",r1.delete())
print("after deletion: elements in queue:")
r1.disp()
print() 
r1.insert(72)
r1.insert(56)
print("after inserting again: elements in circular queue:")
r1.disp()
print()


