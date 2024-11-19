class node:
    def __init__(self,v):
        self.info=v
        self.next=None
class CLL:
    def __init__(self):
        self.start=None
    def insertatlast(self,v):
        n=node(v)
        if self.start==None:
            self.start=n
            n.next=self.start
        else:
            temp=self.start
            while temp.next!=self.start:
                temp=temp.next
            temp.next=n
            n.next=self.start
    def traverse(self):
        temp=self.start
        while temp.next!=self.start:
            print(temp.info,end="-->")
            temp=temp.next
        print(temp.info)
    def insertatbegin(self,v):
        n=node(v)
        temp=self.start
        while temp.next!=self.start:
            temp=temp.next
        n.next=self.start
        temp.next=n
        self.start=n
    def deleteatbegin(self):
        temp=self.start
        while temp.next!=self.start:
            temp=temp.next
        var=self.start
        self.start=var.next
        temp.next=self.start
        del var
    def insertatspecificitem(self,item):
        p=int(input("enter node:"))
        new=node(p)
        temp=self.start
        while temp.info!=item:
            temp=temp.next
        new.next=temp.next
        temp.next=new
    def deletespecificitem(self,item):
        if item==self.start.info:
            self.deleteatbegin()
            return
        else:
            temp=self.start
            while temp.info!=item:
                prev=temp
                temp=temp.next
            prev.next=temp.next
            del temp
    def insertatpos(self,po):
        q=int(input("enter node:"))
        new=node(q)
        if po==1:
            self.insertatbegin(q)
        else:    
            temp=self.start
            for i in range(1,po-1):
                temp=temp.next
            new.next=temp.next
            temp.next=new
    def deleteatpos(self,po):
        if po==1:
            self.deleteatbegin()
            return 
        else:
            temp=self.start
            for i in range(1,po):
                prev=temp
                temp=temp.next
            if temp!=None:
                prev.next=temp.next
                del temp
    def deletelastnode(self):
        temp=self.start
        while temp.next!=self.start:
            prev=temp
            temp=temp.next
        prev.next=self.start
        del temp
    def rev_cll(self):
        prev=self.start
        curr=prev.next
        next1=curr.next
        while curr!=self.start:
            curr.next=prev
            prev=curr
            curr=next1
            if next1!=self.start:
               next1=next1.next
        self.start.next=prev
        self.start=prev
        return self.start
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
            
            
            
        
r1=CLL()
n=int(input("how many nodes you want to create:"))
for i in range(n):
    x=int(input("enter a node:"))
    r1.insertatlast(x)
r1.traverse()
print()
z=int(input("enter node which you want to insert at begin:"))
r1.insertatbegin(z)
r1.traverse()
print()
print("delete begin node:")
r1.deleteatbegin()
r1.traverse()
print()
y=int(input("enter specific node:"))
r1.insertatspecificitem(y)
r1.traverse()
print()
y1=int(input("enter node which you want to delete:"))
r1.deletespecificitem(y1)
r1.traverse()
print()
y2=int(input("enter position where you insert a new node:"))
r1.insertatpos(y2)
r1.traverse()
print()
d=int(input("enter position which you want to delete node:"))
r1.deleteatpos(d)
r1.traverse()
print()
print("delete last node:")
r1.deletelastnode()
r1.traverse()
print()
z1=int(input("enter search element:"))
c=r1.search(z1)
if c==-1:
    print("item is not found")
else:
    print("item is found at position:",c)
r1.rev_cll()
r1.traverse()
            
           
