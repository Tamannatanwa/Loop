n=int(input("enter the number"))
product=1
for i in range (n,0):
    product=product*(n%10)
    n=n//10
print(product)