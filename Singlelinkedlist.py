class node:
    def __init__(self,value):
        self.info=value
        self.next=None
class singlelinkedlist:
    def __init__(self):
        self.start=None
    def insertatlast(self,v):
        a=node(v)
        if self.start==None:
            self.start=a
        else:
            temp=self.start
            while temp.next!=None:
                temp=temp.next
            temp.next=a
    def traverse(self):
        temp=self.start
        while temp!=None:
            print(temp.info,end="-->")
            temp=temp.next
    def insertatbegin(self,v):
        t=node(v)
        t.next=self.start
        self.start=t
        return self.start
    def deleteatbegin(self):
        n=self.start
        self.start=self.start.next
        del n
        return self.start
    def deletelastnode(self):
        temp=self.start
        while temp.next!=None:
            prev=temp
            temp=temp.next
        del temp
        prev.next=None
    def insertatspecificitem(self,item):
        p=int(input("enter node:"))
        new=node(p)
        temp=self.start
        while temp.info!=item:
            temp=temp.next
        new.next=temp.next
        temp.next=new
        return
    def deletespecificitem(self,item):
        if item==self.start.info:
            n=self.start
            self.start=self.start.next
            del n
            return self.start
        else:
           temp=self.start
           while temp.info!=item:
             prev=temp
             temp=temp.next
           if temp!=None:
            prev.next=temp.next
            del temp
       
    def insertatpos(self,pos):
        q=int(input("enter a node:"))
        new=node(q)
        if pos==1:
            new.next=self.start
            self.start=new
            return self.start
        else:    
           temp=self.start
           for i in range(1,pos-1):
            temp=temp.next
           new.next=temp.next
           temp.next=new
    def deleteatpos(self,pos):
        if pos==1:
            n=self.start
            self.start=self.start.next
            del n
            return self.start
        else:
          temp=self.start    
          for i in range(1,pos):
            prev=temp
            temp=temp.next
          if temp!=None:
            prev.next=temp.next
            del temp
          else:
             print("position does not exist")
    def rev_ll(self):
        prev=self.start
        curr=prev.next
        next1=curr.next
        while curr!=None:
            curr.next=prev
            prev=curr
            curr=next1
            if next1!=None:
               next1=next1.next
        self.start.next=None
        self.start=prev
        
        
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
                
            
                
            

        
             
            
                    
r1=singlelinkedlist()
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
r1.deleteatbegin()
print("after deleting beginning node:")
r1.traverse()
print()
y=int(input("enter specific node:"))
r1.insertatspecificitem(y)
r1.traverse()
print()
z=int(input("enter node which you want to delete:"))
r1.deletespecificitem(z)
r1.traverse()
print()
m=int(input("enter position where you insert a new node:"))
r1.insertatpos(m)
r1.traverse()
print()
s1=int(input("enter position which you want to delete node:"))
r1.deleteatpos(s1)
r1.traverse()
print()
r1.deletelastnode()
print("after deleting last node:")
r1.traverse()
print()

z1=int(input("enter search element:"))
c=r1.search(z1)
if c==-1:
    print("element is not found in linkedlist")
else:    
    print("element is found at position:",c)
print()    
print("reverse order of nodes of linkedlist")    
r1.rev_ll()
r1.traverse()
    

