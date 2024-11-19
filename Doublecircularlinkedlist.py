class node:
    def __init__(self,v):
        self.info=v
        self.prev=None
        self.next=None
class DCLlist:
    def __init__(self):
        self.start=None
    def insertatlast(self,v):
        new=node(v)
        if self.start==None:
            self.start=new
            new.next=self.start
            new.prev=self.start
        else:
            temp=self.start
            while temp.next!=self.start:
                temp=temp.next
            temp.next=new
            new.prev=temp
            new.next=self.start
            self.start.prev=new
    def traverse(self):
        temp=self.start
        while temp.next!=self.start:
            print(temp.info,end="-->")
            temp=temp.next
        print(temp.info)    
    def insertatbegin(self,v):
        new=node(v)
        last=self.start.prev
        last.next=new
        new.prev=last
        new.next=self.start
        self.start.prev=new
        self.start=new
    ''' def deleteatbegin(self):
        temp=self.start
        while temp.next!=self.start:
            temp=temp.next
        var=self.start
        self.start=self.start.next
        self.start.prev=var.prev
        temp.next=self.start
        del var'''
    def deleteatbegin(self):
        var=self.start
        self.start=self.start.next
        self.start.prev=var.prev
        var.prev.next=self.start
        del var
    def deletelastnode(self):
        temp=self.start.prev
        temp.prev.next=self.start
        self.start.prev=temp.prev
        del temp
    def insertatspecificitem(self,item):
        v=int(input("enter a node:"))
        new=node(v)
        temp=self.start
        while temp.info!=item:
            temp=temp.next
        new.next=temp.next
        temp.next.prev=new
        temp.next=new
        new.prev=temp
    def deletespecificitem(self,item):
        if item==self.start.info:
            self.deleteatbegin()
            return self.start
        else:
            temp=self.start
            while temp.info!=item:
                pre=temp
                temp=temp.next
            if temp!=None:
                pre.next=temp.next
                temp.next.prev=pre
                del temp
    def insertatpos(self,pos):
        q=int(input("enter node:"))
        new=node(q)
        if pos==1:
            self.insertatbegin(q)
            return
        else:
            temp=self.start
            for i in range(1,pos-1):
                temp=temp.next
            new.next=temp.next
            temp.next.prev=new
            temp.next=new
            new.prev=temp
    def deleteatpos(self,pos):
        if pos==1:
            self.deleteatbegin()
        else:
            temp=self.start
            for i in range(1,pos):
                pre=temp
                temp=temp.next
            if temp!=None:
                pre.next=temp.next
                temp.next.prev=pre
                del temp           
    def search(self,x):
        temp=self.start
        c=0
        while 1:
             if x==temp.info:
                 c=c+1
                 return c
             else:
                 temp=temp.next
                 c=c+1
                 if temp==self.start:
                     break
        return -1
    def rev_dcll(self):
        temp=self.start
        curr=temp.next
        next1=curr.next
        while curr!=self.start:
            curr.next=temp
            curr.prev=next1
            temp=curr
            curr=next1
            if next1!=self.start:
                next1=next1.next
        self.start.next=temp
        self.start=temp
        
    
                
            
        
r1=DCLlist()
t=int(input("how many nodes you want to create:"))
for i in range(t):
   v=int(input("enter a node:"))
   r1.insertatlast(v)
r1.traverse()
print()

x=int(input("enter node which you want to insert at begin:"))
r1.insertatbegin(x)
r1.traverse()
print()
print("after deleting begin node:")
r1.deleteatbegin()
r1.traverse()
print()
y=int(input("enter specific node:"))
r1.insertatspecificitem(y)
r1.traverse()
print()
m=int(input("enter position where you insert a new node:"))
r1.insertatpos(m)
r1.traverse()
print()
m1=int(input("enter position which you want to delete node:"))
r1.deleteatpos(m1)
r1.traverse()
print()

z=int(input("enter specific node which you want to delete:"))
r1.deletespecificitem(z)
r1.traverse()
print()
print("after deleting last node:")
r1.deletelastnode()
r1.traverse()
print()
z1=int(input("enter search item:"))
c=r1.search(z1)
if c==-1:
    print("item is not found")
else:
    print("item is found at position:",c)
r1.rev_dcll()
r1.traverse()








        
                
