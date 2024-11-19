class node:
    def __init__(self,v):
        self.info=v
        self.next=None
        self.prev=None
class doublelinkedlist:
    def __init__(self):
        self.start=None
    def insertatlast(self,v):
        n=node(v)
        if self.start==None:
            self.start=n
        else:
            temp=self.start
            while temp.next!=None:
                temp=temp.next
            temp.next=n
            n.prev=temp
    def traverse(self):
        temp=self.start
        while temp!=None:
            print(temp.info,end="<-->")
            temp=temp.next
    def insertatbegin(self,v):
        t=node(v)
        t.next=self.start
        self.start.prev=t
        self.start=t
        return self.start
    def deleteatbegin(self):
        n=self.start
        self.start=self.start.next
        self.start.prev=None
        del n
        return self.start
    def insertatspecificitem(self,item):
         p=int(input("enter node:"))
         new=node(p)
         temp=self.start
         while temp.info!=item:
            temp=temp.next  
         new.next=temp.next
         temp.next.prev=new
         temp.next=new
         new.prev=temp
         return
    def deletespecificitem(self,item):
        temp=self.start
        if item==temp.info:
            self.deleteatbegin()
            return
        else:    
          while temp!=None and temp.info!=item:
            pre=temp
            temp=temp.next
          if temp!=None:
            pre.next=temp.next
            temp.next.prev=pre
            del temp
          else:
            print("node does not exist")
    def insertatpos(self,pos):
        q=int(input("enter a node:"))
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
          temp=self.start.next
          pre=self.start
          for i in range(1,pos-1):
            temp=temp.next
            pre=pre.next
          pre.next=temp.next
          temp.next.prev=pre
          del temp
    def deletelastnode(self):
        temp=self.start.next
        pre=self.start
        while temp.next!=None:
            temp=temp.next
            pre=pre.next
        pre.next=None
        temp.prev=None
    def search(self,x):
        temp=self.start
        c=0
        while temp!=None:
            if x==temp.info:
                c=c+1
                return c
            else:
                temp=temp.next
                c=c+1
        return -1
    def rev_dll(self):
        curr=self.start
        temp=None
        while curr!=None:
            temp=curr.prev
            curr.prev=curr.next
            curr.next=temp
            curr=curr.prev
        self.start=temp.prev
        return self.start
                
        
        
        
        
r1=doublelinkedlist()
n=int(input("how many nodes you want to create:"))
for i in range(n):
   v=int(input("enter a node:"))
   r1.insertatlast(v)
r1.traverse()
print()
x=int(input("enter node which you want to insert at begin:"))
r1.insertatbegin(x)
r1.traverse()
print()
print("after deleting beginning node:")
r1.deleteatbegin()
r1.traverse()
print()
z=int(input("enter specific item:"))
r1.insertatspecificitem(z)
r1.traverse()
print()
y=int(input("enter item which you want to delete:"))
r1.deletespecificitem(y)
r1.traverse()
print()
k=int(input("enter position which you want to insert node:"))
r1.insertatpos(k)
r1.traverse()
print()
s=int(input("enter position which you want to delete node:"))
r1.deleteatpos(s)
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
r1.rev_dll()
r1.traverse()
