#Program to find the factorial of a number
n=int(input("enter a number="))
f=1

#method1
for x in range(1,n+1):
    f=f*x
print("factorial=",f)

