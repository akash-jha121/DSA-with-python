class binarylist:
    def __init__(self,a,datatype=int):
        self.array=a
        self.size=len(self.array)
        self.datatype=datatype
        for i in range(self.size):
            if type(self.array[i])!=datatype:
                print("not similar type data")
                exit()  
                
    def disp(self):
        print(self.array)

    def binarysearch(self,si):
        beg=0
        end=self.size-1
        while beg<=end:
          mid=(beg+end)//2
          if si==self.array[mid]:
            # print("index of",si,"is:")
             return mid
          elif si<self.array[mid]:
             end=mid-1
          else:
              beg=mid+1
  
        return -1
    def insertitem(self,x):
        self.array.append(x)
        print("one item",x ,"inserted")
        self.size=self.size+1
        return self.array
    def deleteitem(self,x):
        if x in self.array:
          self.array.remove(x)  
          print("one item",x,"deleted")
        else:
           print("item not found")
        return self.array    
            
r1=binarylist([10,23,45,78,87,122])
r1.disp()
y=r1.binarysearch(87)
print("index of search item is:",y)
r1.insertitem(126)
print(r1.deleteitem(45))
print("index of insert element:",r1.binarysearch(126))



                               
                
                
