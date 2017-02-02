list=[None]*5
global topPtr
topPtr=0

def stack_push(data):
    global topPtr
    if (topPtr==len(list)):
        print("list full")
        
    else:
        list[topPtr]=data
        topPtr+=1
    #print(topPtr)
    print(list)
        
def stack_pop():
    global topPtr
    if (topPtr==0):
        print("List is empty")
    else:
        list[topPtr-1]=None
        topPtr-=1
    #print(topPtr)
    print(list)

end=0
while (end==0):
    uin=input("1:Push, 2:Pop")
    if (uin=='1'):
        stack_push(1)
    elif (uin=='2'):
        stack_pop()
    else:
        print("Error")
