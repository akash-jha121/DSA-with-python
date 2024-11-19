class linearlist:
    def __init__(self,a,datatype=int):
        self.array=a
        self.size=len(self.array)
        self.datatype=datatype
        for i in range(self.size):
            if type(self.array[i])!=datatype:
                print("not similar type data")
                exit()
    def display(self):
        print(self.array)
    def bubblesort(self):
        for i in range((self.size)-1):
            for j in range(self.size-i-1):
                if self.array[j]>self.array[j+1]:
                    self.array[j],self.array[j+1]=self.array[j+1],self.array[j]
        return self.array
    def insertitem(self,x):
        self.array.append(x)
        print('one item',x,'is inserted')
        self.size=self.size+1
        return self.array
    def delete(self,m):
        if m in self.array:
           self.array.remove(m)
           print("one item" ,m ,"is deleted")
        else:
            print("item not present in array")
        
    
        
a=[12,67,9,64,34,56,23,45]       
r1=linearlist(a)
r1.display()
print("after sorting:",r1.bubblesort())
r1.insertitem(39)
print("sorted after inserting element:",r1.bubblesort())
r1.delete(133)





