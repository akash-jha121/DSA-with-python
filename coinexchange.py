'''l=[1,2,5,10,20,50,100,200,500,2000]
l1=[]
n=int(input("enter amount:"))
for i in l[-1: :-1]:
    while n>=i:
        n=n-i
        l1.append(i)
print(l1)  
print("minimun no. of denominations:",len(l1))'''


def coinChange(coins, amount):
        if amount<1:
            return 0
        n=len(coins)
        l = [[float('inf') for t in range(amount + 1)] for m in range(n)]
        for i in range(n):
            l[i][0] = 0
        for i in range(n):
            for j in range(1, amount + 1):
                if i > 0:
                     l[i][j] = l[i-1][j]
                if coins[i] <= j:
                     l[i][j] = min(l[i][j], l[i][j - coins[i]] + 1)
        r = l[n-1][amount] if l[n-1][amount] != float('inf') else -1
        return r
r=coinChange([1,2,5,10,20,50,100],89)
print("minimum coins:",r)


        
        
    
