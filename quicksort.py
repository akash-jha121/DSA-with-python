class linearlist:
    def __init__(self,a,datatype=int):
        self.array=a
        self.size=len(self.array)
        self.datatype=datatype
        for k in self.array:
            if type(k)!=datatype:
                print("not similar type data")
                exit()
    def disp(self):
        print(self.array)
    def quick(self,s,e):
        piv=s
        left=s+1
        right=e
        while 1:
            while a[piv]<=a[right] and left<=right:
                right=right-1
            if a[piv]>a[right]:
               a[piv],a[right]=a[right],a[piv]
               piv=right
               right=right-1
            if left> right:
               return piv
            while a[piv]>=a[left] and left<=right:
                left =left+1
            if a[piv]< a[left]:
               a[piv],a[left]=a[left],a[piv]
               piv=left
               left=left+1
            if left> right:
               return piv
    def quicksort(self,s,e):
        if e>s:
            p=self.quick(s,e)
            self.quicksort(s,p-1)
            self.quicksort(p+1,e)
    def insert(self,x) :
        self.array.append(x)
        print("one item",x,"inserted")
        self.size=self.size+1
        return self.array
    def delete(self,y):
        if y in self.array:
            self.array.remove(y)
            print("one item",y,"deleted")
        else:
            print("item",y,"not in array")          
        
a=[1,3,7,8,7,9,32,23]
r1=linearlist(a)
r1.disp()
r1.quicksort(0,len(a)-1)
r1.disp()
r1.insert(6)
r1.quicksort(0,len(a)-1)
r1.disp()
r1.delete(7)








           
                
