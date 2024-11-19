class linearlist:
    def __init__(self,a,datatype=int):
        self.array=a
        self.size=len(self.array)
        self.datatype=datatype
        for k in self.array:
            if type(k)!=datatype:
                print("not similar type data")
                exit()
    def display(self):
        print("before sorting:",self.array)
    def insertionsort(self):
        for k in range(1,self.size):
            item=a[k]
            po=k-1
            while item<a[po] and po>=0:
                a[po+1]=a[po]
                po=po-1
            a[po+1]=item
        return self.array
    def insert(self,x):
        self.array.append(x)
        print("one element",x,"is inserted")
        self.size=self.size+1
        return self.array
    def delete(self,y):
        if y in self.array:
            self.array.remove(y)
            print("element",y,"is deleted")
        else:
            print("element not present in array")
a=[12,23,3,56,11,34]
r1=linearlist(a)
r1.display()
print("after sorting:",r1.insertionsort())
r1.insert(45)
print("sorted after inserting element:",r1.insertionsort())
r1.delete(3)
            



                
