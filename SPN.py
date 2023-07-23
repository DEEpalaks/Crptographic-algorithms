def xor(x,y):
    result=""
    for i in range(len(x)):
        if(x[i]==y[i]):
            result+="0"
        else:
            result+="1"
    return result
def spn(key,plain,pi_s,pi_pi):
    plain_size=len(plain)
    key_matrix=[]
    for i in range(0,len(key),4):
        key_matrix.append(key[i:i+plain_size])
        if(i+plain_size==len(key)):
            break
    print("The key matrix is..........",key_matrix)
    binary_to_hexa={"0000":"0","0001":"1","0010":"2","0011":"3","0100":"4","0101":"5","0110":"6","0111":"7","1000":"8","1001":"9","1010":"A","1011":"B","1100":"C","1101":"D","1110":"E","1111":"F"}
    hexa_to_binary={"0":"0000","1":"0001","2":"0010","3":"0011","4":"0100","5":"0101","6":"0110","7":"0111","8":"1000","9":"1001","A":"1010","B":"1011","C":"1100","D":"1101","E":"1110","F":"1111"}
    w=plain
    for j in range(len(key_matrix)-1):
        u=xor(w,key_matrix[j])
        print("The u value is..........",u)
        o1=""
        for i in range(0,len(w),4):
            o=binary_to_hexa[u[i:i+4]]
            re=pi_s[o]
            o1+=hexa_to_binary[re]
        print("V is..........",o1)
        ref=o1
        w=""
        for k in range(len(o1)):
            w+=ref[pi_pi[k]-1]
        print("W is..........",w)
    result=xor(o1,key_matrix[len(key_matrix)-1])
    return result
plain=input("Enter the plain text")
key=input("Enter the key")
print("Enter the Substitution table")
pi_s={}
for i in range(16):
    a=input("Enter the value")
    b=input("Enter the corresponding substitution")
    pi_s[a]=b
print("Enter the permutation table")
pi_pi=[]
for i in range(16):
    b=int(input("Enter the corresponding permutation"))
    pi_pi.append(b)
result=spn(key,plain,pi_s,pi_pi)
print(result)
