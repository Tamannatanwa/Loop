


n=int(input("enter the number"))
i=n
sum=0
f=1
while n>0:
    r=n%10
    f=f*r
    sum=sum+r
    n=n//10
    r=r-1
if i==sum:
    print(i,"strong number")
else:
    print(i,"not strong number")
