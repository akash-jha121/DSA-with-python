class node:
    def __init__(self,v):
        self.info=v
        self.link=None
class singlelinkedlist:
    def __init__(self):
        self.start=None
    def insertatlast(self,v):
        a=node(v)
        if self.start==None:
            self.start=a
        else:
            temp=self.start
            while temp.link!=None:
                temp=temp.link
            temp.link=a
    def traverse(self):
        temp=self.start
        while temp!=None:
            print(temp.info,end="-->")
            temp=temp.link
    def rev_ll(self):
        prev=self.start
        curr=prev.link
        next1=curr.link
        while curr!=None:
            curr.link=prev
            prev=curr
            curr=next1
            if next1!=None:
               next1=next1.link
        self.start.link=None
        self.start=prev
r1=singlelinkedlist()
n=int(input("how many nodes you want to create:"))
for i in range(n):
   v=int(input("enter a node:"))
   r1.insertatlast(v)
r1.traverse()
print()
r1.rev_ll()
r1.traverse()

        
    
