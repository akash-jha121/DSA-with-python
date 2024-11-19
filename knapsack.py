def knapsack(pft,wt,maxwt):
    n=len(pft)
    l=[[0 for m in range(maxwt+1)]for t in range(n+1)]
    for i in range(1,n+1):
        for j in range(1,maxwt+1):
            if wt[i-1]<=j:
                l[i][j]=max(l[i-1][j],pft[i-1]+l[i-1][j-wt[i-1]])
            else:
                l[i][j]=l[i-1][j]
    return l[n][maxwt]
s=knapsack([10,5,15,7,6,18,3],[2,3,5,7,1,4,1],15)
print("max profit:",s)
