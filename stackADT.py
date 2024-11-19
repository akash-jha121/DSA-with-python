def create_stack():
    stk=[]
    top=None
    return stk
def isempty(stk):
    if len(stk)==0:
        print("stack is empty")
        return
def push(stk,x):
    stk.append(x)
    top=len(stk)-1
    print(x,"pushed in stack")
    return
def pop(stk):
    if(isempty(stk)):
        print("stack is emnpty")
        return
    else:
        a=stk.pop()
        if len(stk)==0:
            top=None      
    return a
def disp(stk):
    if(isempty(stk)):
        print("stack is empty")
    else:
         top=len(stk)-1
         for i in range(top,-1,-1):
            print(stk[i])

stack=create_stack()
push(stack,23)
push(stack,34)
push(stack,98)
push(stack,980)
push(stack,45)
a=pop(stack)
b=pop(stack)
print("removed element:",a)
print("removed element:",b)

disp(stack)
print("TOS:",stack[-1])
