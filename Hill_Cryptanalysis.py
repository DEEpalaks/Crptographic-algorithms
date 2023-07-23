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
def mod_for_matrix(matrix2,n):
    for i in range(len(matrix2[0])):
        for j in range(len(matrix2[0])):
            matrix2[i][j]=modulus(matrix2[i][j],n)
    return matrix2
def inverse_op(det,adj):
    for i in range(len(adj[0])):
        for j in range(len(adj[0])):
            adj[i][j]=modulus(adj[i][j]*det,26)
    return adj
def hill_cryptanalysis(plain,cipher):
    #finding inverse of plain
    if(len(plain[0]))==2:
        det=plain[0][0]*plain[1][1]-plain[0][1]*plain[1][0]
        adj_1=[]
        adj_plain=[]
        for i in range(2):
            for j in range(2):
                if(i==0 and j==0):
                    a1=plain[1][1]
                elif(i==0 and j==1):
                    a1=-1*plain[0][1]
                elif(i==1 and j==0):
                    a1=-1*plain[1][0]
                else:
                    a1=plain[0][0]
                adj_1.append(a1)
            adj_plain.append(adj_1)
            adj_1=[]
        inverse=inverse_op(mod_inverse(det,26),adj)
    else:
        det=(plain[0][0]*(plain[1][1]*plain[2][2]-plain[1][2]*plain[2][1]))-1*(plain[0][1]*(plain[1][0]*plain[2][2]-plain[1][2]*plain[2][0]))+(plain[1][2]*(plain[1][0]*plain[1][1]-plain[2][0]*plain[2][1]))
        adj_2=[]
        adj=[]
        adj_2.append((plain[1][1]*plain[2][2]-plain[2][1]*plain[1][2]))
        adj_2.append(-1*(plain[1][0]*plain[2][2]-plain[1][2]*plain[2][0]))
        adj_2.append((plain[1][0]*plain[2][1]-plain[2][0]*plain[1][1]))
        adj.append(adj_2)
        adj_2=[]
        adj_2.append(-1*(plain[0][1]*plain[2][2]-plain[0][2]*plain[2][1]))
        adj_2.append(plain[0][0]*plain[2][2]-plain[0][2]*plain[2][0])
        adj_2.append(-1*(plain[0][0]*plain[2][1]-plain[0][1]*plain[2][0]))
        adj.append(adj_2)
        adj_2=[]
        adj_2.append(plain[0][1]*plain[1][2]-plain[0][2]*plain[1][1])
        adj_2.append(-1*(plain[0][0]*plain[1][2]-plain[0][2]*plain[1][0]))
        adj_2.append(plain[0][0]*plain[1][1]-plain[0][1]*plain[1][0])
        adj.append(adj_2)
        adj_2=[]
        adj=mod_for_matrix(adj,26)
        inverse=inverse_op(mod_inverse(det,26),adj)
    sum=0;
    list_2=[]
    key=[]
    for i in range(len(plain[0])):
        for j in range(len(plain[0])):
            for k in range(len(plain[0])):
                sum+=cipher[i][k]*inverse[k][j]
            list_2.append(sum)
        key.append(list_2)
        list_2=[]
    key=mod_for_matrix(key,26)
    return key
if(__name__=="__main__"):
    list_2=[]
    listt=[]
    print("Enter the plain text matrix")
    for i in range(3):
        for j in range(3):
            list_2.append(int(input("Enter")))
        listt.append(list_2)
        list_2=[]
    print("plain text is..........",listt)
    print("Enter the cipher text matrix")
    list_2=[]
    listtt=[]
    for i in range(3):
        for j in range(3):
            list_2.append(int(input("Enter")))
        listtt.append(list_2)
        list_2=[]
    print("cipher text is..........",listtt)
    key=hill_cryptanalysis(listt,listtt)
    print("Key value is..........",key)
    
