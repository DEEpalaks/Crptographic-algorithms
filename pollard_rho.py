import math
def func(a):
    return(math.pow(a,2)+1)
def pollard_rho(n,x):
    y=x
    if(n==1):
        return 1
    elif(n%2==0):
        return 2
    else:
        d=1
        while(d==1 or d==n):
           x=func(x)%n
           g=func(y)
           y=func(g)%n
           d=math.gcd(int(abs(x-y)),n)
           if(d<n):
               if(d>1):
                   return d
           else:
               return 0
n=int(input("Enter the n value"))
x=int(input("Enter the x value"))
result=pollard_rho(n,x)
if(result!=0):
    print("Answer is equal to ",result,int(n/result))
else:
    print("Failure")

