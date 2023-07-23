import math
def inverse(a,n):
    for i in range(1,n+1):
        if((a*i-1)%n==0):
            return i
def shanks(g,n,alpha,beta):
    m=math.ceil(math.sqrt(n))
    j_matrix=[]
    j_1=[]
    for i in range(m):
        j_1.append(i)
        j_1.append((alpha**(m*i))%g)
        j_matrix.append(j_1)
        j_1=[]
    for i in range(len(j_matrix)):
        for j in range(len(j_matrix)-1):
            if(j_matrix[j][1]>j_matrix[j+1][1]):
                temp=j_matrix[j]
                j_matrix[j]=j_matrix[j+1]
                j_matrix[j+1]=temp
    i_matrix=[]
    i_1=[]
    alpha_inverse=inverse(alpha,g)
    for i in range(m):
        i_1.append(i)
        i_1.append((beta*(alpha_inverse)**i)%g)
        i_matrix.append(i_1)
        i_1=[]
    for i in range(len(i_matrix)):
        for j in range(len(i_matrix)-1):
            if(i_matrix[j][1]>i_matrix[j+1][1]):
                temp=i_matrix[j]
                i_matrix[j]=i_matrix[j+1]
                i_matrix[j+1]=temp
    result=[]
    for i in range(len(j_matrix)):
        for j in range(len(i_matrix)):
            if(j_matrix[i][1]==i_matrix[j][1]):
                result.append(j_matrix[i][0])
                result.append(i_matrix[j][0])
    answer=m*result[0]+result[1]
    return answer
g=int(input("Enter the g value"))
n=int(input("Enter the n value"))
alpha=int(input("Enter the alpha value"))
beta=int(input("Enter the beta value"))
print(shanks(n+1,n,alpha,beta))
        
