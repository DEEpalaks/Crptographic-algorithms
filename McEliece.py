import numpy as np
def key(G,S,P):
    G_1=np.dot(np.dot(S,G),P).tolist()
    return G_1
def enc(X,G_1,e):
    inter=np.dot(X,G_1).tolist()
    encrypt=[]
    for i in range(len(inter)):
        encrypt.append(inter[i]+e[i])
    return encrypt
def decode(Y):
    e1=Y[-1]^Y[-3]^Y[-5]^Y[-7]
    e2=Y[-2]^Y[-3]^Y[-6]^Y[-7]
    e3=Y[-4]^Y[-5]^Y[-6]^Y[-7]
    e=str(e1)+str(e2)+str(e3)
    e=int(e,2)-1
    if(Y[e]==0):
        Y[e]=1
    else:
        Y[e]=0
    return Y
def dec(encrypt,P,e,k,S):
    P_inv=np.linalg.inv(P).tolist()
    for i in range(len(P_inv)):
        for j in range(len(P_inv[0])):
            P_inv[i][j]=int(P_inv[i][j])
    Y_1=np.dot(encrypt,P_inv).tolist()
    Y=decode(Y_1)
    x_0=Y[:k]
    S_inv=np.linalg.inv(S).tolist()
    for i in range(len(S_inv)):
        for j in range(len(S_inv[0])):
            S_inv[i][j]=int(S_inv[i][j])
    x=np.dot(x_0,S_inv).tolist()
    return x
k=int(input("Enter the k value"))
n=int(input("Enter the n value"))
temp=[]
G=[]
S=[]
P=[]
print("Enter the G matrix")
G=[[1,0,0,0,1,1,0],[0,1,0,0,1,0,1],[0,0,1,0,0,1,1],[0,0,0,1,1,1,1]]
print("Enter the S matrix")
S=[[1,1,0,1],[1,0,0,1],[0,1,1,1],[1,1,0,0]]
print("Enter the P matrix")
P=[[0,1,0,0,0,0,0],[0,0,0,1,0,0,0],[0,0,0,0,0,0,1],[1,0,0,0,0,0,0],[0,0,1,0,0,0,0],[0,0,0,0,0,1,0],[0,0,0,0,1,0,0]]
print("Enter the message")
X=[]
for i in range(k):
    X.append(int(input("Enter")))
print("Enter the error")
e=[]
for i in range(n):
    e.append(int(input("Enter")))
l=key(G,S,P)
encryption=enc(X,l,e)
print(G)
print(S)
print(P)
for i in range(len(encryption)):
    encryption[i]=encryption[i]%2
print("Encryption=",encryption)
decryption=dec(encryption,P,e,k,S)
for i in range(len(decryption)):
    decryption[i]=decryption[i]%2
print("Decryption=",decryption)

