# 1+x/1!+x2/2!+...xn/n!


x=int(input("enter the number"))
n=int(input("enter the number"))
sum=0
fac=1
i=1
while i<=n:
    fac=fac*i
    sum=sum+x**n/fac
    i=i+1
print(1+sum)