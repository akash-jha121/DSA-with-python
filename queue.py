class queue:
    def __init__(self,s):
        self.size=s
        self.l=[0 for i in range(s)]
        self.rear=-1
        self.front=-1
    def insert(self,item):
        if self.rear==self.size-1:
            print("queue is full")
            return
        else:
            self.rear=self.rear+1
            self.l[self.rear]=item
            if self.front==-1:
                self.front=0
    def delete(self):
        if self.rear==-1 and self.front==-1:
            print("queue is empty")
            return
        item=self.l[self.front]
        if self.front==self.rear:
            self.front=-1
            self.rear=-1
            return item
        else:
            self.front=self.front+1
            return item    
    def disp(self):
        if self.front==-1 and self.rear==-1:
            print("queue is empty")
        else:
            for i in range(self.front,self.rear+1):
                print(self.l[i],end=" ") 
r1=queue(4)
r1.insert(23) 
r1.insert(243)
r1.insert(68)
r1.insert(87)
r1.disp() 
print()
print("delete item:",r1.delete())
print("delete item:",r1.delete())
r1.disp()
            
