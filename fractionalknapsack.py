def fracknap(pft,wt,mwt):
    res=[i/j for i, j in zip(pft,wt)]
    n=len(wt)
    ind=list(range(n))
    ind.sort(key=lambda i: res[i],reverse=True)
    p=0
    l=[]
    for i in ind:
        if wt[i]<=mwt:
            p=p+pft[i]
            mwt=mwt-wt[i]
        else:
            p =p+ pft[i] * (mwt / wt[i])
            break
    
    return p
s=fracknap([10,5,15,7,6,18,3],[2,3,5,7,1,4,1],15)
print('MAX PROFIT:',s)

    
