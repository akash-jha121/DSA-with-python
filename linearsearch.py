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
        print(self.array)
    def linearsearch(self,si):
        for j in range(self.size):
            if si==self.array[j]:
             return j
        return -1   
            
    def insertitem(self,x):
        self.array.append(x)
        print("one item",x,"is inserted")
        self.size =self.size+1
        return self.array
    def deleteitem(self,y):
        if y in self.array:
             self.array.remove(y)
             print("one item is deleted")
        else:
            print("item not found")

r1=linearlist([1,3,5,7,12,8])
r1.display()
print("search item is found at index :",r1.linearsearch(12))
r1.insertitem(45)
r1.deleteitem(12)
print("index of inserting item:",r1.linearsearch(45))




  
