a=int(input("enter the number"))
count=0
for i in range(a,0):
    if a%i==0:
        count+=1
if count==2:
    print(a,"is prim numbere")
else:
    print(a,"is not prim number")
        
    