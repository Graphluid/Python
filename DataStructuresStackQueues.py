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
    print(topPtr)
    print(list)
        
def stack_pop():
    global topPtr
    if (topPtr==0):
        print("List is empty")
    else:
        list[topPtr-1]=None
        topPtr-=1
    print(topPtr)
    print(list)
    
print(list)

    
