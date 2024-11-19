def lcs(x, y):
    n = len(x)
    m = len(y)
    l=[[0]*(m+1)for i in range(n+1)]
    m1=0
    
    for i in range(1, n+1):
        for j in range(1, m+1):
            if x[i-1] == y[j-1]:
                l[i][j] = 1 + l[i-1][j-1]
                m1=max(m1,l[i][j])
            else:
                l[i][j]=0
    
    return m1

s = lcs('abdfghij', 'zxabfghijlm')
print(s)
