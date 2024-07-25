
N=int(input())
L=[]

I=int(input())
if (I==0 ):
    if (len(L)>0):
        L.sort()
        print(L.pop(0))
    else:
        print(0)
    
else:
    L.append(I)

