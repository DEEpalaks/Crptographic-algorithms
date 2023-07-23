def modulus(a,n):
    if(a>=0):
        return a%n
    else:
        d=abs(a)
        d=int(d/n)+1
        return (d*n+a)    
def mod_inverse(a,n):
    for i in range(1,n+1):
        if((a*i-1)%n==0):
            return i
def inverse_op(det,adj):
    for i in range(len(adj[0])):
        for j in range(len(adj[0])):
            adj[i][j]=modulus(adj[i][j]*det,26)
    return adj
def hill_encryption(plain,key):
    plain_1=plain.lower()
    if(len(key[0])==2 and len(plain_1)%2!=0):
        plain_1+='x'
    elif(len(plain_1)%3!=0):
        plain_1+='x'*(len(plain_1)%3)
    plain_matrix=[]
    list_1=[]
    for i in range(len(plain_1)):
        if(len(list_1)<len(key[0])):
            list_1.append(ord(plain_1[i])-97)
        else:
            plain_matrix.append(list_1)
            list_1=[]
            list_1.append(ord(plain_1[i])-97)
    cipher=[]
    cipher_1=[]
    sum=0
    for i in plain_matrix:
        for j in range(len(key)):
            for k in range(len(key[0])):
                sum+=i[k]*key[k][j]
            sum=sum%26+65
            cipher_1.append(chr(sum))
            sum=0
        cipher.append(cipher_1)
        cipher_1=[]
    return cipher
def hill_decryption(cipher,key):
    cipher_1=cipher.upper()
    cipher_matrix=[]
    list_1=[]
    for i in range(len(cipher_1)):
        if(len(list_1)<len(key[0])):
            list_1.append(ord(cipher_1[i])-65)
        else:
            cipher_matrix.append(list_1)
            list_1=[]
            list_1.append(ord(cipher_1[i])-65)
    cipher_matrix.append(list_1)
    if(len(key[0])==2):
        det=key[0][0]*key[1][1]-key[0][1]*key[1][0]
        adj=[]
        adj_2=[]
        for i in range(2):
            for j in range(2):
                if(i==0 and j==0):
                    a1=key[1][1]
                elif(i==1 and j==1):
                    a1=key[0][0]
                elif(i==0 and j==1):
                    a1=-1*key[i][j]
                else:
                    a1=-1*key[i][j]
                adj_2.append(a1)
            adj.append(adj_2)
            adj_2=[]
        inverse=inverse_op(mod_inverse(det,26),adj)
    else:
        det=(key[0][0]*(key[1][1]*key[2][2]-key[1][2]*key[2][1]))-1*(key[0][1]*(key[1][0]*key[2][2]-key[1][2]*key[2][0]))+(key[1][2]*(key[1][0]*key[1][1]-key[2][0]*key[2][1]))
        adj_2=[]
        adj=[]
        for i in range(3):
            for j in range(3):
                if(i==0):
                    i1=1
                    i2=2
                elif(i==1):
                    i1=0
                    i2=2
                else:
                    i1=0
                    i2=1
                if(j==0):
                    j1=1
                    j2=2
                elif(j==1):
                    j1=0
                    j2=2
                else:
                    j1=0
                    j2=1
                a1=key[i][j]*(key[i1][j1]*key[i2][j2]-key[i1][j2]*key[i2][j1])
                if((i+j)%2!=0):
                    a1=-1*a1
                adj_2.append(a1)
            adj.append(adj_2)
            adj_2=[]
        inverse=inverse_op(mod_inverse(det,26),adj)
    plain=[]
    plain_2=[]
    sum=0
    for i in cipher_matrix:
        for j in range(len(inverse)):
            for k in range(len(inverse[0])):
                sum+=i[k]*inverse[k][j]
            sum=sum%26+97
            plain_2.append(chr(sum))
            sum=0
        plain.append(plain_2)
        plain_2=[]
    return plain
n=int(input("Enter the key size"))
key_1=[]
key=[]
for i in range(n):
    for j in range(n):
        key_1.append(int(input("Enter the ij key value")))
    key.append(key_1)
    key_1=[]
plain=input("Enter the plain text")
sum=hill_encryption(plain,key)
result=""
for i in range(n):
    for j in range(n):
        result+=sum[i][j]
print("The cipher text is..........",result)
sum=hill_decryption(result,key)
result_1=""
for i in range(n):
    for j in range(n):
        result_1+=sum[i][j]
print("The plain text is..........",result_1)
