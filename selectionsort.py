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
    def selectionsort(self):
        for i in range(self.size-1):
            for k in range(i+1,self.size):
                if self.array[i]>self.array[k]:
                    self.array[i],self.array[k]=self.array[k],self.array[i]
        return self.array
    def insert(self,x):
      self.array.append(x)
      print("one item",x,"inserted")
      self.size=self.size+1
      return self.array
    def delete(self,y):
        if y in self.array:
            self.array.remove(y)
            print("one item" ,y,"deleted")
        else:
            print("item not found")
        return self.array    
a=[1,5,9,4,17,8,12,3]    
r1=linearlist(a)
r1.display()
print("after sorting:",r1.selectionsort())
r1.insert(7)
print("sorted after inserting element:",r1.selectionsort())
r1.delete(12)

