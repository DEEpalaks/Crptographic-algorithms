import math as m
def inverse(a,n):
    for i in range(1,n+1):
        if(a*i-1)%n==0:
            return i
def gamma(alpha,k):
    return(pow(alpha,k)%p)
def delta(x,a,gaama,k,p):
    k_inv=inverse(k,p-1)
    return ((x-a*gaama)*k_inv)%(p-1)
def elgamal_signature(p,alpha,a):
    beta=int(pow(alpha,a))%p
    k=int(input("Enter the k value"))
    x=int(input("Enter the message value"))
    g=int(gamma(alpha,k))
    d=int(delta(x,a,g,k,p))
    print("Signature(x,k)=",g,d)
    ver=(pow(beta,g))*(pow(g,d))%p
    if(ver==pow(alpha,x)%p):
        print("Valid")
    else:
        print("Invalid")
p=int(input("Enter the p value"))
alpha=int(input("Enter the primitive root value"))
a=int(input("Enter the a value"))
elgamal_signature(p,alpha,a)
