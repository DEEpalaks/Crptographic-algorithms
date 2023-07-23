import math
def pollard_p_1(n,b):
    a=2
    i=2
    for j in range(i,b+1):
        a=(a**j)%n
        d=math.gcd(a-1,n)
        if(d>1):
            return d
    return 0
n=int(input("Enter n value"))
b=math.floor(math.sqrt(n))
result=pollard_p_1(n,b)
if(result!=0):
    print("Answers are ",result,int(n/result))
else:
    print("Failure")
