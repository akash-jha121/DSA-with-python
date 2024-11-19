class tower_hanoi:
    def toh(self,size,beg,end,aux):
        if size>1:
            self.toh((size-1),beg,aux,end)
            
            print(beg,"->",end)
            self.toh((size-1),aux,end,beg)
        else:
             print(beg,"->",end)
    def disp(self,beg,end,aux):
        print(beg,"->",end)
        
    
r1=tower_hanoi()
n=int(input("enter size:"))
r1.toh(n,"B","E","A")
print("total moves=",2**n-1)






        
