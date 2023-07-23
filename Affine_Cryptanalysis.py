import Affine_cryptography as af
def modulus(a,n):
    if(a>=0):
        return a%n
    else:
        c=abs(a)
        d=int(c//n)
        return (d+1)*n+a
def affine_cryptanalysis(cipher):
    a_set=[1,3,5,7,9,11,15,17,19,21,23,25]
    statistics=['E','T','A','O','I','N','S','H','R','D','L']
    check=-1
    m=1
    occurence=[]
    for i in cipher:
        if(i not in occurence):
            occurence.append(i)
            occurence.append(cipher.count(i))
    for i in range(int(len(occurence)/2)):
        for j in range(int(len(occurence)/2)-1):
            if(occurence[2*j+1]<occurence[2*j+3]):
                temp=occurence[2*j]
                occurence[2*j]=occurence[2*j+2]
                occurence[2*j+2]=temp
                temp=occurence[2*j+1]
                occurence[2*j+1]=occurence[2*j+3]
                occurence[2*j+3]=temp
    equ_1=[]
    for i in a_set:
        equ_1.append(i)
        equ_1.append(modulus((ord(occurence[0])-65-(ord(statistics[0])-65)*i),26))
    result=[]
    print(occurence)
    for j in range(1,len(statistics)):
        for k in range(1,int(len(occurence)/2)):
            letter=ord(occurence[2*k])-65
            for b in range(int(len(equ_1)/2)):
                if(modulus((ord(statistics[j])-65)*equ_1[2*b]+equ_1[2*b+1],26)==letter):
                    result.append(equ_1[2*b])
                    result.append(equ_1[2*b+1])
                    result.append(ord(statistics[j])-65)
                    result.append(letter)
                    check=1
                    break
            if(check==1):
                break
        if(check==1):
            return result
            break
        elif(j==len(statistics)-1):
            print("No keys are possible for the mentioned sequence of letters")
if(__name__=="__main__"):
    cipher=input("Enter the sequence of cipher text")
    result=affine_cryptanalysis(cipher)
    print("a value is..........",result[0],"b value is..........",result[1],result[2],result[3])
    print(af.affine_decryption(cipher,result[0],result[1]))
    
        
        
