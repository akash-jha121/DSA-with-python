class linearlist:
    def __init__(self,arr,datatype=int):
        self.array=arr
        self.size=len(self.array)
        self.datatype=datatype
        for k in self.array:
            if type(k)!=datatype:
                print("not similar type data")
                exit()
    def display(self):
        print(self.array)
    def merge_sort(self,arr):
      if len(arr)>1:
        l_arr=arr[0:len(arr)//2]
        r_arr=arr[len(arr)//2: ]
        self.merge_sort(l_arr)
        self.merge_sort(r_arr)
        i=j=k=0
        while i<len(l_arr) and j<len(r_arr):
               if l_arr[i]<r_arr[j]:
                 arr[k]=l_arr[i]
                 i=i+1
               else:
                 arr[k]=r_arr[j]
                 j=j+1
               k=k+1
        while i<len(l_arr):
          arr[k]=l_arr[i]
          k=k+1
          i=i+1
        while j<len(r_arr):
          arr[k]=r_arr[j]
          j=j+1
          k=k+1
        return arr
    def insert(self,x):
       self.array.append(x)
       print("one item",x,"inserted")
       self.size=self.size+1
       return self.array
    def delete(self,y):
        if y in self.array:
            self.array.remove(y)
            print("item",y,"deleted")
        else:
            print("item not in array")
        #return self.array   
       
arr=[1,3,2,5,6,4,9,8,12]          
r1=linearlist(arr)
r1.display()
r1.merge_sort(arr)
r1.display()
r1.insert(11)
r1.merge_sort(arr)
r1.display()
r1.delete(8)







